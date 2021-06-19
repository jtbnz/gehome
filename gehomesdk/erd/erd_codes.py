"""ERD Codes for GE appliances"""
import enum
from typing import Union

@enum.unique
class ErdCode(enum.Enum):
    """
    ERD codes for GE kitchen appliance properties.
    These were mostly lifted from ERD.smali in the the GE SmartHQ app v1.0.3.13
    """
    APPLIANCE_TYPE = "0x0008"
    CLOCK_FORMAT = "0x0006"
    CLOCK_TIME = "0x0005"
    MODEL_NUMBER = "0x0001"
    SABBATH_MODE = "0x0009"
    SERIAL_NUMBER = "0x0002"
    SOUND_LEVEL = "0x000a"
    TEMPERATURE_UNIT = "0x0007"
    USER_INTERFACE_LOCKED = "0x0004"
    UNIT_TYPE = "0x0035"

    # Low-level-type things
    UNKNOWN_0099 = "0x0099"
    WIFI_MODULE_SW_VERSION = "0x0100"
    WIFI_MODULE_SW_VERSION_AVAILABLE = "0x0101"
    ACM_UPDATING = "0x0102"
    APPLIANCE_SW_VERSION = "0x0103"
    APPLIANCE_SW_VERSION_AVAILABLE = "0x0104"
    APPLIANCE_UPDATING = "0x0105"
    LCD_SW_VERSION = "0x0106"
    LCD_SW_VERSION_AVAILABLE = "0x0107"
    LCD_UPDATING = "0x0108"

    # Dishwasher Codes
    DISHWASHER_CYCLE_NAME = "0x301c"
    DISHWASHER_CYCLE_STATE = "0x300e"
    DISHWASHER_OPERATING_MODE = "0x3001"
    DISHWASHER_PODS_REMAINING_VALUE = "0x301f"
    DISHWASHER_RINSE_AGENT = "0x3003"
    DISHWASHER_USER_SETTING = "0x3007"
    DISHWASHER_TIME_REMAINING = "0xd004"
    DISHWASHER_UNKNOWN_3009 = "0x3009"
    DISHWASHER_UNKNOWN_301d = "0x301d"
    DISHWASHER_UNKNOWN_3035 = "0x3035"
    DISHWASHER_DOOR_STATUS = "0x3037"
    DISHWASHER_UNKNOWN_3045 = "0x3045"
    DISHWASHER_UNKNOWN_304E = "0x304e"
    DISHWASHER_UNKNOWN_3100 = "0x3100"
    DISHWASHER_UNKNOWN_D003 = "0xd003"

    # Laundry Codes
    LAUNDRY_MACHINE_STATE = "0x2000"
    LAUNDRY_SUB_CYCLE = "0x2001"
    LAUNDRY_END_OF_CYCLE = "0x2002"
    LAUNDRY_TIME_REMAINING = "0x2007"
    LAUNDRY_WASHER_TANK_STATUS = "0x2008"
    LAUNDRY_WASHER_TANK_SELECTED = "0x2009"
    LAUNDRY_DELAY_TIME_REMAINING = "0x2010"
    LAUNDRY_DOOR = "0x2012"
    LAUNDRY_WASHER_DOOR_LOCK = "0x2013"
    LAUNDRY_CYCLE = "0x200a"
    LAUNDRY_DRYER_DRYNESS_LEVEL = "0x201a"
    LAUNDRY_DRYER_TUMBLE_STATUS = "0x201b"
    LAUNDRY_DRYER_UNKNOWN201C = "0x201c"
    LAUNDRY_UNKNOWN201D = "0x201d"
    LAUNDRY_WASHER_SOIL_LEVEL = "0x2015"
    LAUNDRY_WASHER_WASHTEMP_LEVEL = "0x2016"
    LAUNDRY_WASHER_SPINTIME_LEVEL = "0x2017"
    LAUNDRY_WASHER_RINSE_OPTION = "0x2018"
    LAUNDRY_DRYER_TEMPERATURE_OPTION = "0x2019"
    LAUNDRY_DRYER_UNKNOWN2022 = "0x2022"
    LAUNDRY_DRYER_UNKNOWN2023 = "0x2023"
    LAUNDRY_UNKNOWN2038 = "0x2038"
    LAUNDRY_REMOTE_STATUS = "0x2039"
    LAUNDRY_UNKNOWN2040 = "0x2040"
    LAUNDRY_UNKNOWN2041 = "0x2041"
    LAUNDRY_DRYER_DRYNESSNEW_LEVEL = "0x204d"
    LAUNDRY_DRYER_TEMPERATURENEW_OPTION = "0x2050"
    LAUNDRY_DRYER_UNKNOWN2051 = "0x2051"
    LAUNDRY_DRYER_UNKNOWN2052 = "0x2052"
    LAUNDRY_DRYER_TUMBLENEW_STATUS = "0x2053"
    LAUNDRY_WASHER_UNKNOWN2069 = "0x2069"
    LAUNDRY_DRYER_WASHERLINK_CYCLE = "0x206b"
    LAUNDRY_DRYER_WASHERLINK_STATUS = "0x206c"
    LAUNDRY_DRYER_WASHERLINK_CONTROL = "0x206e"
    LAUNDRY_DRYER_UNKNOWN206F = "0x206f"

    # Fridge codes
    AIR_FILTER_STATUS = "0x101c"
    DOOR_STATUS = "0x1016"
    FRIDGE_MODEL_INFO = "0x101d"
    HOT_WATER_IN_USE = "0x1018"
    HOT_WATER_SET_TEMP = "0x1011"
    HOT_WATER_STATUS = "0x1010"
    ICE_MAKER_BUCKET_STATUS = "0x1007"
    ICE_MAKER_CONTROL = "0x100a"
    SETPOINT_LIMITS = "0x100b"
    CURRENT_TEMPERATURE = "0x1004"
    TEMPERATURE_SETTING = "0x1005"
    TURBO_COOL_STATUS = "0x100f"
    TURBO_FREEZE_STATUS = "0x100e"
    WATER_FILTER_STATUS = "0x1009"

    # Oven codes
    ACTIVE_F_CODE_STATUS = "0x5005"
    CONVECTION_CONVERSION = "0x5003"
    ELAPSED_ON_TIME = "0x5004"
    END_TONE = "0x5001"
    HOUR_12_SHUTOFF_ENABLED = "0x5000"
    KEY_PRESSED = "0x5006"
    LIGHT_BAR = "0x5002"
    LOWER_OVEN_AVAILABLE_COOK_MODES = "0x520b"
    LOWER_OVEN_COOK_MODE = "0x5200"
    LOWER_OVEN_COOK_TIME_REMAINING = "0x5204"
    LOWER_OVEN_CURRENT_STATE = "0x5201"
    LOWER_OVEN_DELAY_TIME_REMAINING = "0x5202"
    LOWER_OVEN_DISPLAY_TEMPERATURE = "0x5209"
    LOWER_OVEN_ELAPSED_COOK_TIME = "0x5208"
    LOWER_OVEN_KITCHEN_TIMER = "0x5205"
    LOWER_OVEN_PROBE_DISPLAY_TEMP = "0x5203"
    LOWER_OVEN_PROBE_PRESENT = "0x5207"
    LOWER_OVEN_REMOTE_ENABLED = "0x520a"
    LOWER_OVEN_USER_TEMP_OFFSET = "0x5206"
    LOWER_OVEN_WARMING_DRAWER_STATE = "0x520c"
    LOWER_OVEN_RAW_TEMPERATURE = "0x520d"
    OVEN_CONFIGURATION = "0x5007"
    OVEN_MODE_MIN_MAX_TEMP = "0x5008"
    UPPER_OVEN_AVAILABLE_COOK_MODES = "0x510b"
    UPPER_OVEN_COOK_MODE = "0x5100"
    UPPER_OVEN_COOK_TIME_REMAINING = "0x5104"
    UPPER_OVEN_CURRENT_STATE = "0x5101"
    UPPER_OVEN_DELAY_TIME_REMAINING = "0x5102"
    UPPER_OVEN_DISPLAY_TEMPERATURE = "0x5109"
    UPPER_OVEN_ELAPSED_COOK_TIME = "0x5108"
    UPPER_OVEN_KITCHEN_TIMER = "0x5105"
    UPPER_OVEN_PROBE_DISPLAY_TEMP = "0x5103"
    UPPER_OVEN_PROBE_PRESENT = "0x5107"
    UPPER_OVEN_REMOTE_ENABLED = "0x510a"
    UPPER_OVEN_USER_TEMP_OFFSET = "0x5106"
    UPPER_OVEN_WARMING_DRAWER_STATE = "0x510c"
    UPPER_OVEN_RAW_TEMPERATURE = "0x510d"
    WARMING_DRAWER_STATE = "0x5009"

    COOKTOP_CONFIG = "0x551c"
    COOKTOP_STATUS = "0x5520"

    PRECISION_COOKING_PROBE_CONTROL_MODE = "0x5670"
    PRECISION_COOKING_PROBE_STATUS = "0x5671"
    PRECISION_COOKING_PROBE_TEMP_TARGET = "0x5672" #R/W, int 4 places
    PRECISION_COOKING_PROBE_TEMP_CURRENT = "0x5673"
    PRECISION_COOKING_PROBE_TIME_TARGET = "0x5674" #R/W, int 4 places
    PRECISION_COOKING_START_SOUS_VIDE_TIMER_ACTIVE_STATUS = "0x5675" #R/W, int 2 places
    PRECISION_COOKING_PROBE_TIME_CURRENT = "0x5676"
    PRECISION_COOKING_PROBE_TARGET_TIME_REACHED = "0x5677"
    PRECISION_COOKING_PROBE_BATTERY_STATUS = "0x5678"

    CLOSED_LOOP_COOKING_CONFIGURATION = "0x5770"

    # Microwave
    MICROWAVE_RECIPE_STATUS = "0x5300"
    MICROWAVE_UNKNOWN_5C12 = "0x5c12"
    MICROWAVE_REMOTE_ENABLE = "0x5c14"
    MICROWAVE_UNKNOWN_5C18 = "0x5c18"
    # Lots more in 0x5Cxx

    # Hood

    # Advantium
    ADVANTIUM_KITCHEN_TIME_REMAINING = "0x0050"
    # ADVANTIUM_MIN_MAX_TEMP = "0x5008" #See: OVEN_MODE_MIN_MAX_TEMP
    # ADVANTIUM_DISPLAY_TEMP = "0x5109"  #See: UPPER_OVEN_DISPLAY_TEMPERATURE
    # ADVANTIUM_REMOTE_ENABLED = "0x510a" #See: UPPER_OVEN_REMOTE_ENABLED
    ADVANTIUM_REMOTE_COOK_MODE_CONFIG = "0x5400"
    ADVANTIUM_COOK_STATUS = "0x5401"
    ADVANTIUM_COOK_SETTING = "0x5402"
    ADVANTIUM_COOK_TIME_REMAINING = "0x5403"
    ADVANTIUM_COOK_TIME_ADJUST = "0x5404"
    ADVANTIUM_PRECISION_VERSION = "0x5405"
    ADVANTIUM_UNKNOWN_5406 = "0x5406"
    ADVANTIUM_COOK_TIME_MIN_MAX = "0x5407"
    ADVANTIUM_MICROWAVE_MIN_MAX = "0x5408"
    ADVANTIUM_PRECISION_MIN_MAX = "0x5409"
    ADVANTIUM_KITCHEN_TIMER_MIN_MAX = "0x540a"
    
ErdCodeType = Union[ErdCode, str]
