import unittest
import sys, os
sys.path.append(os.getcwd())
from happy_birthday_ga import get_objective_sentence


class TestGetObjectiveSentence(unittest.TestCase):
    # User name is not given
    def test_success_get_default(self):
        expected = get_objective_sentence()
        actual = 'Happy birthday, upura!'
        self.assertEqual(expected, actual)

    # User name is given
    def test_success_get_user_name(self):
        sys.argv.append('Shinzo Abe')
        expected = get_objective_sentence()
        actual = 'Happy birthday, Shinzo Abe!'
        self.assertEqual(expected, actual)
        del sys.argv[1:]

    # User name is given (Not a string)
    def test_success_get_not_string(self):
        sys.argv.append(111)
        expected = get_objective_sentence()
        actual = 'Happy birthday, 111!'
        self.assertEqual(expected, actual)
        del sys.argv[1:]

if __name__ == "__main__":
    unittest.main()