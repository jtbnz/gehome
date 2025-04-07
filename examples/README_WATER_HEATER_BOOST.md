# Water Heater Boost Mode Example

This README provides instructions on how to use the water heater boost example script to control the boost mode of GE water heaters.

## Prerequisites

Before using this example, make sure you have:

1. Installed the GE Home SDK with the water heater boost functionality
2. Updated your credentials in the `examples/credentials.py` file with your GE appliance account information:
   ```python
   USERNAME = "your-email@example.com"
   PASSWORD = "your-password"
   REGION = "US"  # or your region
   ```
3. A GE water heater connected to your account

## Using the Example Script

The `water_heater_boost_example.py` script allows you to monitor and control the boost mode of your GE water heaters.

### Basic Usage

To run the script in monitoring mode (will run for 10 minutes by default):

```bash
python water_heater_boost_example.py
```

### Enabling Boost Mode

To enable the boost mode on your water heater:

```bash
python water_heater_boost_example.py --boost true
```

### Disabling Boost Mode

To disable the boost mode on your water heater:

```bash
python water_heater_boost_example.py --boost false
```

### Setting Runtime

You can specify how long the script should run (in seconds) using the `--runtime` parameter:

```bash
# Run for 5 minutes (300 seconds)
python water_heater_boost_example.py --runtime 300

# Enable boost mode and run for 2 minutes
python water_heater_boost_example.py --boost true --runtime 120
```

## Understanding the Output

When you run the script, it will:

1. Connect to the GE appliance cloud service
2. Discover all appliances associated with your account
3. Identify water heaters and add them to the control list
4. Display the current boost mode status of each water heater
5. If requested, enable or disable the boost mode
6. Monitor and log any state changes

Example output:

```
2025-04-08 10:05:00 INFO     Waiting for water heaters to be discovered...
2025-04-08 10:05:30 INFO     Water heater detected: Water Heater (serial: AB123456C)
2025-04-08 10:05:30 INFO     Added water heater to control list. Total water heaters: 1
2025-04-08 10:05:30 INFO     Current boost mode: DISABLED
2025-04-08 10:05:30 INFO     Found 1 water heater(s)
2025-04-08 10:05:30 INFO     Enabling boost mode on water heater: Water Heater (serial: AB123456C)
2025-04-08 10:05:31 INFO     Successfully enabling boost mode on Water Heater (serial: AB123456C)
2025-04-08 10:05:31 INFO     Waiting 5 seconds for the change to take effect...
2025-04-08 10:05:36 INFO     Current boost mode after change: ENABLED
2025-04-08 10:05:38 INFO     Boost mode after full update: ENABLED
2025-04-08 10:05:40 INFO     Water heater state change detected in Water Heater (serial: AB123456C). Updated keys: ErdCode.WH_HEATER_BOOST_MODE
2025-04-08 10:05:40 INFO     Boost mode changed to: ENABLED
```

## Troubleshooting

If you encounter issues:

1. Make sure your credentials are correct
2. Verify that your water heater is online and connected to your account
3. Check that the water heater supports the boost mode functionality
4. Increase the logging level for more detailed information by changing:
   ```python
   logging.basicConfig(level=logging.DEBUG, ...)  # Change INFO to DEBUG
   ```

## Understanding the Implementation

The example script demonstrates:

1. How to connect to the GE appliance cloud service
2. How to discover and identify water heaters
3. How to read the current boost mode status
4. How to set the boost mode using the boost control ERD code
5. How to monitor state changes in real-time

This serves as a practical example of how to use the new water heater boost functionality added to the GE Home SDK.

## Technical Details

Based on testing with real GE water heaters, we've learned the following:

1. `WH_HEATER_BOOST_MODE` (0x4220) is a read-only ERD code that indicates the current boost mode status
2. `WH_HEATER_BOOST_CONTROL` (0x4221) is a read-write ERD code used to control the boost mode
3. `WH_HEATER_VACATION_FALLBACK_MODE` (0x4023) is the vacation fallback mode setting

The example script has been updated to use the correct ERD codes for reading and writing the boost mode:
- Use `WH_HEATER_BOOST_MODE` to read the current boost mode status
- Use `WH_HEATER_BOOST_CONTROL` to enable or disable the boost mode

When you enable the boost mode, the water heater will temporarily increase the water temperature to provide more hot water. The boost mode status will change to reflect the current state of the boost operation.

### Important Notes

#### Timing Considerations

The example script now includes a 5-second delay after setting the boost mode before reading it again. This is important because:

1. The water heater may take a few seconds to process the command
2. The cloud service may need time to update its state
3. Reading the boost mode immediately after setting it may return the old value

The script also performs a full update request after the delay to ensure it has the latest state from the appliance. This helps prevent errors and ensures the script can accurately report the current boost mode status.

#### Value Encoding

The boost mode values must be properly encoded as hexadecimal strings when sent to the appliance. The converter has been updated to use the `erd_encode_int` function to ensure the values are properly formatted. This is critical for the appliance to accept the commands.

If you encounter an error like:
```
GeRequestError: There was an error while processing a message: Code=400, Reason=None, Message={"kind":"websocket#api", ... "reason":"value is not valid"}}
```

It means the value format is incorrect. The proper encoding ensures that:
1. Integer values are converted to hexadecimal strings
2. The values have the correct length (1 byte for boost mode)
3. The values are formatted according to the appliance's expectations
