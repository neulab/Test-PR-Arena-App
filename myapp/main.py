# myapp/main.py
from utils import format_message

def greet(name):
    """
    Creates a greeting message for the given name.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A formatted greeting message
    """
    message = f"Hello, {name}!"
    return format_message(message)

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    greeting = greet(user_name)
    print(greeting)
