import unittest

def is_palindrome(un_mot):
    return True

class PalindromeTest(unittest.TestCase):

    def test_world(self):
        self.assertEqual(is_palindrome("kayak"), True)
        self.assertEqual(is_palindrome("toto"), False)