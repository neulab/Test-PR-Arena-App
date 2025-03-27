# tests/test_utils.py
import unittest
import re
from datetime import datetime
import pytz

# Add the parent directory to the path so we can import the myapp module
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from myapp.utils import format_message, get_timezone

class TestUtils(unittest.TestCase):
    def test_format_message_includes_timezone(self):
        """Test that the formatted message includes timezone information"""
        message = "Hello, Test!"
        formatted = format_message(message)
        
        # Check that the message contains the original message
        self.assertIn(message, formatted)
        
        # Check that the message contains a timestamp with timezone
        # Format should be: Hello, Test! (at YYYY-MM-DD HH:MM:SS TZ±HHMM)
        timestamp_pattern = r'\(at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]+[+-]\d{4}\)'
        self.assertTrue(re.search(timestamp_pattern, formatted), 
                        f"Timestamp with timezone not found in: {formatted}")
    
    def test_format_message_with_custom_timezone(self):
        """Test that the formatted message uses the specified timezone"""
        message = "Hello, Test!"
        timezone = "America/New_York"
        formatted = format_message(message, timezone)
        
        # Extract the timezone from the formatted message
        match = re.search(r'\(at .* ([A-Z]+[+-]\d{4})\)', formatted)
        self.assertTrue(match, f"Timezone not found in: {formatted}")
        
        # Verify that the timezone is correct
        # The exact string might vary (EST/EDT depending on daylight saving)
        # but should contain the correct UTC offset for New York
        tz_string = match.group(1)
        
        # Get the expected offset for the timezone
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        expected_offset = now.strftime("%z")
        
        self.assertIn(expected_offset, tz_string, 
                     f"Expected timezone offset {expected_offset} not found in {tz_string}")

if __name__ == '__main__':
    unittest.main()
