import unittest

from rearrange_spaces import rearrange_spaces


class TestRearrangeSpaces(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(
            rearrange_spaces("  this   is  a sentence "),
            "this   is   a   sentence"
        )

    def test_single_word(self):
        self.assertEqual(
            rearrange_spaces("   word"),
            "word   "
        )

    def test_two_words(self):
        self.assertEqual(
            rearrange_spaces("a  b"),
            "a  b"
        )
    def test_three_words(self):
        self.assertEqual(
            rearrange_spaces("a  b cc"),
            "a b cc "
        )


if __name__ == '__main__':
    unittest.main()
