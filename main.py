import json

from WordLadder import WordLadder


def main():
    with open("word_list.json") as f:
        word_list = json.load(f)

    my_word_ladder = WordLadder(word_list)
    my_word_ladder.starting_word = "wheat"
    my_word_ladder.ending_word = "bread"

    my_word_ladder.find_shortest_word_ladder()


if __name__ == '__main__':
    main()
