import json
import unittest

from WordLadder import WordLadder


class TestWordLadder(unittest.TestCase):

    def setUp(self) -> None:
        with open("word_list.json") as f:
            self.word_list = json.load(f)
        self.my_word_ladder = WordLadder(self.word_list)

    def test_starting_word_validation_valid(self):
        self.my_word_ladder.starting_word = "playground"
        self.assertEqual(self.my_word_ladder.starting_word, "playground")

    def test_starting_word_validation_invalid(self):
        with self.assertRaises(Exception):
            self.my_word_ladder.starting_word = "ooooo"

    def test_ending_word_validation_starting_word_not_set(self):
        with self.assertRaises(Exception):
            self.my_word_ladder.ending_word = "play"

    def test_ending_word_validation_starting_word_different_length(self):
        self.my_word_ladder.starting_word = "world"
        with self.assertRaises(Exception):
            self.my_word_ladder.ending_word = "play"

    def test_ending_word_validation_invalid(self):
        self.my_word_ladder.starting_word = "task"
        with self.assertRaises(Exception):
            self.my_word_ladder.ending_word = "ooooo"

    def test_ending_word_validation_same_start_and_end(self):
        self.my_word_ladder.starting_word = "boot"
        with self.assertRaises(Exception):
            self.my_word_ladder.ending_word = "boot"

    def test_ending_word_validation_valid(self):
        self.my_word_ladder.starting_word = "task"
        self.my_word_ladder.ending_word = "play"
        self.assertEqual(self.my_word_ladder.ending_word, "play")

    def test_one_char_word_difference_true(self):
        self.assertTrue(WordLadder._are_strings_diff_by_only_one_char("play", "plao"))

    def test_one_char_word_difference_false(self):
        self.assertFalse(WordLadder._are_strings_diff_by_only_one_char("play", "pkao"))
        self.assertFalse(WordLadder._are_strings_diff_by_only_one_char("play", "play"))

    def test_char_difference_count(self):
        self.assertEqual(WordLadder._count_character_differences_in_strings("play", "play"), 0)
        self.assertEqual(WordLadder._count_character_differences_in_strings("paay", "play"), 1)
        self.assertEqual(WordLadder._count_character_differences_in_strings("alay", "pley"), 2)
        self.assertEqual(WordLadder._count_character_differences_in_strings("pkay", "alau"), 3)
        self.assertEqual(WordLadder._count_character_differences_in_strings("play", "yalp"), 4)

    def test_find_word_ladder_one_char_diff(self):
        self.my_word_ladder.starting_word = "task"
        self.my_word_ladder.ending_word = "talk"
        self.assertEqual(self.my_word_ladder.return_word_ladders(), {'task': ['talk']})

    def test_find_word_ladder_one_char_common1(self):
        self.my_word_ladder.starting_word = "boot"
        self.my_word_ladder.ending_word = "shoe"
        self.assertEqual(self.my_word_ladder.return_word_ladders(), {'boot': ['soot'],
                                                                     'shot': ['shoe'],
                                                                     'soot': ['shot']})

    def test_find_word_ladder_one_char_common2(self):
        self.my_word_ladder.starting_word = "warm"
        self.my_word_ladder.ending_word = "cold"
        self.assertEqual(self.my_word_ladder.return_word_ladders(),
                         {'card': ['cord'],
                          'cord': ['cold'],
                          'corm': ['cord'],
                          'ward': ['card', 'word'],
                          'warm': ['ward', 'worm'],
                          'wold': ['cold'],
                          'word': ['cord', 'wold'],
                          'worm': ['corm', 'word']})


if __name__ == '__main__':
    unittest.main()
