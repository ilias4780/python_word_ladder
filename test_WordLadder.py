import json
import unittest

from WordLadder import WordLadder


class TestWordLadder(unittest.TestCase):

    def setUp(self) -> None:
        with open("word_dict.json") as f:
            word_dict = json.load(f)
        self.my_word_ladder = WordLadder(word_dict)

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

    def test_find_word_ladder_one_char_diff(self):
        self.my_word_ladder.starting_word = "task"
        self.my_word_ladder.ending_word = "talk"
        self.assertEqual(self.my_word_ladder.find_shortest_word_ladder(), "task -> talk")

    def test_find_word_ladder_one_char_common(self):
        self.my_word_ladder.starting_word = "boot"
        self.my_word_ladder.ending_word = "shoe"
        self.assertEqual(self.my_word_ladder.find_shortest_word_ladder(), "boot -> soot -> shot -> shoe")

    def test_find_word_ladder_no_chars_common_four_letters(self):
        self.my_word_ladder.starting_word = "warm"
        self.my_word_ladder.ending_word = "cold"
        self.assertEqual(self.my_word_ladder.find_shortest_word_ladder(), "warm -> ward -> card -> cord -> cold")

    def test_find_word_ladder_five_letters(self):
        self.my_word_ladder.starting_word = "wheat"
        self.my_word_ladder.ending_word = "bread"
        self.assertEqual(self.my_word_ladder.find_shortest_word_ladder(), "wheat -> cheat -> creat -> cread -> bread")

    def test_find_word_ladder_five_letters_more_levels(self):
        self.my_word_ladder.starting_word = "table"
        self.my_word_ladder.ending_word = "crown"
        self.assertEqual(self.my_word_ladder.find_shortest_word_ladder(),
                         "table -> cable -> carle -> carls -> carps -> corps -> coops -> crops -> crows -> crown")

    def test_find_word_ladder_difficult_case(self):
        self.my_word_ladder.starting_word = "charge"
        self.my_word_ladder.ending_word = "comedo"
        self.assertEqual(self.my_word_ladder.find_shortest_word_ladder(),
                         "charge -> charre -> charrs -> chirrs -> shirrs -> shiers -> shyers -> sayers -> payers -> "
                         "papers -> papery -> popery -> popely -> pomely -> comely -> comedy -> comedo")

    def test_unsolvable_scenario(self):
        self.my_word_ladder.starting_word = "electroencephalographically"
        self.my_word_ladder.ending_word = "hydroxydesoxycorticosterone"
        with self.assertRaises(Exception):
            self.my_word_ladder.find_shortest_word_ladder()


if __name__ == '__main__':
    unittest.main()
