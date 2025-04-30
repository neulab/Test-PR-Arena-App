import unittest
from utils import format_message

class TestFormatMessage(unittest.TestCase):

    def test_format_message_utc(self):
        message = "Test message"
        formatted_message = format_message(message, timezone="UTC")
        self.assertTrue("UTC" in formatted_message)

    def test_format_message_pst(self):
        message = "Test message"
        formatted_message = format_message(message, timezone="US/Pacific")
        self.assertTrue("PST" in formatted_message or "PDT" in formatted_message)

    def test_format_message_default_timezone(self):
        message = "Test message"
        formatted_message = format_message(message)
        self.assertTrue("UTC" in formatted_message)

if __name__ == '__main__':
    unittest.main()
