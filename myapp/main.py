# myapp/main.py
import argparse
from utils import format_message

def greet(name, timezone="UTC"):
    """
    Creates a greeting message for the given name.

    Args:
        name (str): The name to greet
        timezone (str): The timezone to use (default: UTC)

    Returns:
        str: A formatted greeting message
    """
    message = f"Hello, {name}!"
    return format_message(message, timezone)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greet a user with a timezone.")
    parser.add_argument("name", help="The name of the user to greet.")
    parser.add_argument("--timezone", default="UTC", help="The timezone to use (default: UTC).")
    args = parser.parse_args()

    greeting = greet(args.name, args.timezone)
    print(greeting)

