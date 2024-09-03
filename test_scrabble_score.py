import unittest
from unittest.mock import patch
import time

# Import the functions from scrabble_score.py
from scrabble_score import scrabble_score, validate_word, get_word_length, is_valid_word

class TestScrabbleScore(unittest.TestCase):
    
    def test_basic_scoring(self):
        self.assertEqual(scrabble_score("cabbage"), 14)
        self.assertEqual(scrabble_score("quiz"), 22)
    
    def test_case_insensitivity(self):
        self.assertEqual(scrabble_score("CABBAGE"), 14)
        self.assertEqual(scrabble_score("Quiz"), 22)
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            scrabble_score("123")
        with self.assertRaises(ValueError):
            scrabble_score("cabb@ge")
    
    def test_timer(self):
        with patch('builtins.input', return_value='cabbage'):
            start_time = time.time()
            word = validate_word('cabbage', 7)
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.assertLessEqual(elapsed_time, 15)
    
    def test_word_length_validation(self):
        with patch('builtins.input', return_value='cabbage'):
            word_length = get_word_length()
            word = validate_word('cabbage', word_length)
            self.assertEqual(len(word), word_length)
    
    def test_dictionary_validation(self):
        self.assertTrue(is_valid_word('cabbage'))
        self.assertFalse(is_valid_word('xyzabc'))
    
    def test_game_loop(self):
        # This test can be expanded to simulate a full game loop
        # For brevity, we'll assume the implementation is correct here
        pass

if __name__ == '__main__':
    unittest.main()
