# myapp/utils.py
import datetime

def format_message(message):
    """
    Formats a message by adding a timestamp.
    
    Args:
        message (str): The message to format
        
    Returns:
        str: The formatted message with a timestamp
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
