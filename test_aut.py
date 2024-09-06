import unittest
from unittest.mock import patch
from scrabble_score import scrabble_score, get_word_length, validate_word, is_valid_word, game_loop

class TestScrabbleScore(unittest.TestCase):
    def test_valid_word(self):
        self.assertEqual(scrabble_score('hello'), 8, "Word 'hello' should score 8 points (h=4, e=1, l=1+1, o=1)")
        self.assertEqual(scrabble_score('quiz'), 22, "Word 'quiz' should score 22 points (q=10, u=1, i=1, z=10)")

    def test_empty_string(self):
        with self.assertRaises(ValueError, msg="Empty string should raise a ValueError"):
            scrabble_score('')

    def test_non_alpha_characters(self):
        with self.assertRaises(ValueError, msg="Non-alphabetic characters should raise a ValueError"):
            scrabble_score('123')

    def test_case_insensitive(self):
        self.assertEqual(scrabble_score('HeLLo'), 8, "Word 'HeLLo' should be case insensitive and score 8 points")

class TestGetWordLength(unittest.TestCase):
    def test_word_length(self):
        for _ in range(100):  # Test multiple times to cover the randomness
            length = get_word_length()
            self.assertTrue(3 <= length <= 7, f"Word length {length} should be between 3 and 7")

class TestValidateWord(unittest.TestCase):
    def test_valid_length(self):
        self.assertEqual(validate_word('word', 4), 'word', "Word 'word' has the correct length")

    def test_invalid_length(self):
        with self.assertRaises(ValueError, msg="Word length mismatch should raise a ValueError"):
            validate_word('word', 5)

class TestIsValidWord(unittest.TestCase):
    def test_valid_word(self):
        self.assertTrue(is_valid_word('hello'), "'hello' is a valid word")

    def test_invalid_word(self):
        self.assertFalse(is_valid_word('qwerty'), "'qwerty' is not a valid word")

class TestNTLK(unittest.TestCase):
    def test_nltk(self):
        try:
            import nltk
            nltk.data.find('corpora/words.zip')
        except LookupError:
            self.fail("NLTK words corpus not found.")




if __name__ == '__main__':
    unittest.main(verbosity=2)
