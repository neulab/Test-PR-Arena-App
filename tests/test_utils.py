import unittest
from myapp.utils import format_message

class TestUtils(unittest.TestCase):
    def test_format_message_default_timezone(self):
        message = "Hello, User!"
        formatted_message = format_message(message)
        self.assertIn("UTC", formatted_message)
        self.assertIn(message, formatted_message)

    def test_format_message_specific_timezone(self):
        message = "Hello, User!"
        formatted_message = format_message(message, timezone='US/Eastern')
        self.assertTrue("EST" in formatted_message or "EDT" in formatted_message)
        self.assertIn(message, formatted_message)

if __name__ == '__main__':
    unittest.main()

