# myapp/utils.py
import datetime
import pytz

DEFAULT_TIMEZONE = pytz.UTC

def format_message(message, timezone=DEFAULT_TIMEZONE):
    """
    Formats a message by adding a timestamp with timezone.
    
    Args:
        message (str): The message to format
        timezone (datetime.tzinfo): The timezone to use (default: UTC)
        
    Returns:
        str: The formatted message with a timestamp
    """
    current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S %Z%z")
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


