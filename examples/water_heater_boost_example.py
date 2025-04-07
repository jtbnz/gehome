"""
Water Heater Boost Mode Example

This example demonstrates how to control the boost mode of a GE water heater.
It connects to the GE appliances using the websocket client, identifies water heaters,
and allows toggling the boost mode on and off.
"""

import aiohttp
import asyncio
import logging
import argparse
from typing import Any, Dict, Tuple
from credentials import USERNAME, PASSWORD, REGION

from gehomesdk import (
    EVENT_ADD_APPLIANCE,
    EVENT_APPLIANCE_STATE_CHANGE,
    EVENT_APPLIANCE_INITIAL_UPDATE,
    ErdApplianceType,
    ErdCode,
    ErdCodeType,
    GeAppliance,
    GeWebsocketClient
)

from gehomesdk.erd.values.water_heater import ErdWaterHeaterBoostMode

_LOGGER = logging.getLogger(__name__)

# Global variable to store water heater appliances
water_heaters = []

async def log_state_change(data: Tuple[GeAppliance, Dict[ErdCodeType, Any]]):
    """Log changes in appliance state"""
    appliance, state_changes = data
    
    # Only log changes for water heaters
    if appliance.appliance_type == ErdApplianceType.WATER_HEATER:
        updated_keys = ', '.join([str(s) for s in state_changes])
        _LOGGER.info(f'Water heater state change detected in {appliance}. Updated keys: {updated_keys}')
        
        # If boost mode changed, log the new value
        if ErdCode.WH_HEATER_BOOST_MODE in state_changes:
            boost_mode = state_changes[ErdCode.WH_HEATER_BOOST_MODE]
            _LOGGER.info(f'Boost mode changed to: {boost_mode.name}')

async def detect_water_heater(appliance: GeAppliance):
    """
    Detect water heater appliances and store them in the global list.
    Also log the current boost mode and state if available.
    """
    if appliance.appliance_type == ErdApplianceType.WATER_HEATER:
        _LOGGER.info(f'Water heater detected: {appliance}')
        
        # Add to global list if not already there
        if appliance not in water_heaters:
            water_heaters.append(appliance)
            _LOGGER.info(f'Added water heater to control list. Total water heaters: {len(water_heaters)}')
        
        # Try to get current boost mode
        try:
            boost_mode = appliance.get_erd_value(ErdCode.WH_HEATER_BOOST_MODE)
            _LOGGER.info(f'Current boost mode: {boost_mode.name}')
        except Exception as e:
            _LOGGER.warning(f'Could not get boost mode: {e}')

async def do_periodic_update(appliance: GeAppliance):
    """Request a full state update every minute for water heaters"""
    if appliance.appliance_type == ErdApplianceType.WATER_HEATER:
        _LOGGER.debug(f'Registering update callback for water heater {appliance}')
        while True:
            await asyncio.sleep(60)
            _LOGGER.debug(f'Requesting update for water heater {appliance}')
            await appliance.async_request_update()

async def toggle_boost_mode(client, enable: bool):
    """Toggle boost mode on all detected water heaters"""
    if not water_heaters:
        _LOGGER.warning("No water heaters detected yet. Please wait...")
        return
    
    boost_mode = ErdWaterHeaterBoostMode.ENABLED if enable else ErdWaterHeaterBoostMode.DISABLED
    action = "Enabling" if enable else "Disabling"
    
    for heater in water_heaters:
        _LOGGER.info(f"{action} boost mode on water heater: {heater}")
        try:
            # Use WH_HEATER_BOOST_CONTROL (0x4221) to set the boost mode
            # WH_HEATER_BOOST_MODE (0x4220) is read-only
            await heater.async_set_erd_value(ErdCode.WH_HEATER_BOOST_CONTROL, boost_mode)
            _LOGGER.info(f"Successfully {action.lower()} boost mode on {heater}")
            
            # Wait 5 seconds for the change to take effect
            _LOGGER.info("Waiting 5 seconds for the change to take effect...")
            await asyncio.sleep(5)
            
            # Read the boost mode again to verify the change
            try:
                current_boost_mode = heater.get_erd_value(ErdCode.WH_HEATER_BOOST_MODE)
                _LOGGER.info(f"Current boost mode after change: {current_boost_mode.name}")
                
                # Request a full update to ensure we have the latest state
                await heater.async_request_update()
                await asyncio.sleep(2)  # Wait a bit for the update to complete
                
                # Read the boost mode one more time
                updated_boost_mode = heater.get_erd_value(ErdCode.WH_HEATER_BOOST_MODE)
                _LOGGER.info(f"Boost mode after full update: {updated_boost_mode.name}")
            except Exception as e:
                _LOGGER.warning(f"Could not verify boost mode change: {e}")
        except Exception as e:
            _LOGGER.error(f"Failed to set boost mode: {e} on {heater}")

async def monitor_and_control(args):
    """Main function to monitor and control water heaters"""
    client = GeWebsocketClient(USERNAME, PASSWORD, REGION)
    client.add_event_handler(EVENT_APPLIANCE_INITIAL_UPDATE, detect_water_heater)
    client.add_event_handler(EVENT_APPLIANCE_STATE_CHANGE, log_state_change)
    client.add_event_handler(EVENT_ADD_APPLIANCE, do_periodic_update)

    async with aiohttp.ClientSession() as session:
        # Start the client
        client_task = asyncio.create_task(client.async_get_credentials_and_run(session))
        
        # Wait for water heaters to be discovered
        _LOGGER.info("Waiting for water heaters to be discovered...")
        await asyncio.sleep(30)
        
        if not water_heaters:
            _LOGGER.warning("No water heaters found after 30 seconds")
        else:
            _LOGGER.info(f"Found {len(water_heaters)} water heater(s)")
        
        # If boost mode argument was provided, toggle it
        if args.boost is not None:
            await toggle_boost_mode(client, args.boost)
        
        # If no action was specified, just monitor
        if args.boost is None and args.runtime == 0:
            _LOGGER.info("No action specified. Monitoring water heater state for 10 minutes...")
            await asyncio.sleep(600)  # 10 minutes
        else:
            # Run for the specified time
            if args.runtime > 0:
                _LOGGER.info(f"Running for {args.runtime} seconds...")
                await asyncio.sleep(args.runtime)
        
        # Cancel the client task
        client_task.cancel()
        try:
            await client_task
        except (asyncio.CancelledError, StopAsyncIteration):
            _LOGGER.debug("Client task cancelled")

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Control GE Water Heater Boost Mode')
    parser.add_argument('--boost', type=lambda x: x.lower() == 'true', 
                        choices=[True, False], 
                        help='Set boost mode: true to enable, false to disable')
    parser.add_argument('--runtime', type=int, default=0,
                        help='How long to run the script in seconds (default: 0 means run indefinitely if no action, or exit after action)')
    return parser.parse_args()

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(levelname)-8s %(message)s')
    
    # Parse arguments
    args = parse_arguments()
    
    # Run the main function
    asyncio.run(monitor_and_control(args))
