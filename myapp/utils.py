# myapp/utils.py
import datetime
import pytz
from .config import TIMEZONE

def format_message(message, timezone=TIMEZONE):
    """
    Formats a message by adding a timestamp with timezone information.
    
    Args:
        message (str): The message to format
        timezone (str): The timezone to use for the timestamp (default is 'UTC')
        
    Returns:
        str: The formatted message with a timestamp
    """
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

