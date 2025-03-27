# myapp/utils.py
import datetime
import pytz

# Default timezone configuration
DEFAULT_TIMEZONE = 'UTC'

def get_timezone():
    """
    Returns the configured timezone.
    
    Returns:
        str: The timezone to use
    """
    return DEFAULT_TIMEZONE

def format_message(message, timezone=None):
    """
    Formats a message by adding a timestamp with timezone information.
    
    Args:
        message (str): The message to format
        timezone (str, optional): The timezone to use. Defaults to the configured timezone.
        
    Returns:
        str: The formatted message with a timestamp and timezone
    """
    if timezone is None:
        timezone = get_timezone()
    
    tz = pytz.timezone(timezone)
    current_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z%z")
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

