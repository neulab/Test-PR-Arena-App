import unittest
from datetime import datetime
from utils import format_message
import pytz

class TestUtils(unittest.TestCase):
    def test_format_message_with_timezone(self):
        # Test with default UTC timezone
        result = format_message("Test")
        self.assertIn("UTC", result)
        
        # Test with specific timezone
        result = format_message("Test", tz="America/New_York")
        self.assertTrue("EST" in result or "EDT" in result, 
                      f"Expected EST or EDT in result, got: {result}")
        
    def test_timezone_format(self):
        # Verify the timestamp format includes timezone info
        result = format_message("Test")
        self.assertRegex(result, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Za-z]+\+\d{4}")

if __name__ == '__main__':
    unittest.main()

