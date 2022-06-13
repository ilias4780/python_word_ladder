import json

from WordLadder import WordLadder


def main():
    with open("word_dict.json") as f:
        word_dict = json.load(f)

    my_word_ladder = WordLadder(word_dict)
    my_word_ladder.starting_word = "charge"
    my_word_ladder.ending_word = "comedo"

    my_word_ladder.find_shortest_word_ladder()


if __name__ == '__main__':
    main()
