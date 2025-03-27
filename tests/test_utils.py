import unittest
from datetime import datetime, timedelta
import pytz
from myapp.utils import format_message, DEFAULT_TIMEZONE

class TestUtils(unittest.TestCase):
    def test_format_message_with_timezone(self):
        # Test with default timezone (UTC)
        message = "Test message"
        formatted = format_message(message)
        self.assertIn("UTC", formatted)
        
        # Test with different timezone
        est = pytz.timezone('US/Eastern')
        formatted_est = format_message(message, est)
        self.assertTrue("EST" in formatted_est or "EDT" in formatted_est)
        
    def test_default_timezone_is_utc(self):
        self.assertEqual(DEFAULT_TIMEZONE, pytz.UTC)

if __name__ == '__main__':
    unittest.main()

