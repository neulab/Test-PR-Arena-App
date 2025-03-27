# myapp/utils.py
import datetime
import pytz

def format_message(message):
    """
    Formats a message by adding a timestamp with timezone information.
    
    Args:
        message (str): The message to format
        
    Returns:
        str: The formatted message with a timestamp
    """
    timezone = pytz.timezone('UTC')  # Default to UTC
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

