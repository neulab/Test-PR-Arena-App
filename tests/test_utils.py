import unittest
from myapp.utils import format_message
import os
import pytz
import datetime

class TestUtils(unittest.TestCase):
    def test_format_message_with_timezone(self):
        os.environ['APP_TIMEZONE'] = 'America/New_York'
        message = format_message("Hello, User!")
        expected_time = datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%Y-%m-%d %H:%M:%S %Z%z")
        self.assertIn(expected_time, message)

    def test_format_message_with_default_timezone(self):
        message = format_message("Hello, User!")
        expected_time = datetime.datetime.now(pytz.timezone('UTC')).strftime("%Y-%m-%d %H:%M:%S %Z%z")
        self.assertIn(expected_time, message)

if __name__ == '__main__':
    unittest.main()
