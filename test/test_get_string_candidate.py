import unittest
import sys, os
sys.path.append(os.getcwd())
from happy_birthday_ga import get_string_candidate


class TestGetStringCandidate(unittest.TestCase):
    def test_get_string_candidate(self):
        string_candidate = get_string_candidate()
        expected = len(string_candidate)
        actual = 26 + 1
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()