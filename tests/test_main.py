# tests/test_main.py
import unittest
import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from myapp.main import greet

class TestMain(unittest.TestCase):
    def test_greet_includes_timezone(self):
        """Test that the greeting includes timezone information"""
        name = "Test User"
        greeting = greet(name)
        
        # Check that the greeting contains the name
        self.assertIn(name, greeting)
        
        # Check that the greeting contains a timestamp with timezone
        # Format should be: Hello, Test User! (at YYYY-MM-DD HH:MM:SS TZ±HHMM)
        timestamp_pattern = r'\(at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [A-Z]+[+-]\d{4}\)'
        self.assertTrue(re.search(timestamp_pattern, greeting), 
                        f"Timestamp with timezone not found in: {greeting}")

if __name__ == '__main__':
    unittest.main()
