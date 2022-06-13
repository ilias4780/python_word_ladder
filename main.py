import json

from WordLadder import WordLadder


def main():
    with open("word_list.json") as f:
        word_list = json.load(f)

    my_word_ladder = WordLadder(word_list)
    my_word_ladder.starting_word = "warm"
    my_word_ladder.ending_word = "cold"

    ladders = my_word_ladder.return_word_ladders()


if __name__ == '__main__':
    main()
