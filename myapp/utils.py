# myapp/utils.py
import datetime
from pytz import timezone

DEFAULT_TIMEZONE = 'UTC'

def format_message(message, tz=DEFAULT_TIMEZONE):
    """
    Formats a message by adding a timestamp with timezone.
    
    Args:
        message (str): The message to format
        tz (str): Timezone string (default: 'UTC')
        
    Returns:
        str: The formatted message with a timestamp
    """
    tz_obj = timezone(tz)
    current_time = datetime.datetime.now(tz_obj).strftime("%Y-%m-%d %H:%M:%S %Z%z")
    return f"{message} (at {current_time})"

def get_message_length(message):
    """
    Returns the length of the given message.
    
    Args:
        message (str): The message to measure
        
    Returns:
        int: The length of the message
    """
    return len(message)


