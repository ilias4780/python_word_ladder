import copy
import json
import pathlib

from anytree import Node


class WordLadder:
    """
    Word ladder class that finds all possible, but also most efficient word path between a starting and an ending
    english word, when supplied with a list of english words.

    :param word_dict: Dictionary of english words. As keys it has the length of the words (strings), as values it has
    dictionaries. The inner dictionaries consist of the word as key and the adjacent words as values.
    """

    def __init__(self, word_dict: dict):
        # create placeholders
        self._ending_word = None
        self._starting_word = None
        self.word_dictionary = word_dict
        self.word_ladder_dict = dict()
        self._nodes = dict()

    @property
    def starting_word(self):
        return self._starting_word

    @starting_word.setter
    def starting_word(self, new_starting_word):
        """
        Sets the starting word for the calculation. Before doing that, it validates that the word is part of the
        used word list.

        :param new_starting_word: Starting word for the path calculation
        """
        if new_starting_word in self.word_dictionary[str(len(new_starting_word))].keys():
            self._starting_word = new_starting_word
        else:
            raise Exception("Please enter a valid starting word.")

    @property
    def ending_word(self):
        return self._ending_word

    @ending_word.setter
    def ending_word(self, new_ending_word):
        """
        Sets the ending word for the calculation. Starting word must be set first. It, also, validates that the word is
        the same length as the starting word and part of the used word list.

        :param new_ending_word: Ending word for the path calculation
        """
        if not self.starting_word:
            raise Exception("Please enter a starting word first.")
        elif len(new_ending_word) != len(self.starting_word):
            raise Exception(f"Please enter an ending word with the same length as the starting word. Starting word is "
                            f"{len(self.starting_word)} characters long.")
        elif new_ending_word == self.starting_word:
            raise Exception("Ending word cannot be the same as starting word.")
        elif new_ending_word not in self.word_dictionary[str(len(new_ending_word))].keys():
            raise Exception("Please enter a valid ending word.")
        else:
            self._ending_word = new_ending_word

    @staticmethod
    def process_word_list(word_list):
        """
        Processes the passed word list into a word dictionary, with keys the length of words and values dictionaries
        that have the words as keys and all adjacent words as their values.

        :param word_list: List of words
        :return: dict
        """
        word_dictionary = dict()
        for word in word_list:
            if len(word) not in word_dictionary:
                word_dictionary[len(word)] = {word: list()}
            else:
                word_dictionary[len(word)][word] = list()
        processed_word_dictionary = copy.deepcopy(word_dictionary)
        for length, word_dict in word_dictionary.items():
            print(f"working for length {length}")
            for word in word_dict.keys():
                processed_word_dictionary[length][word] = WordLadder._find_adjacent_words(word, word_dictionary)

        export_path = pathlib.Path(__file__).resolve().parent
        with open(export_path.joinpath("word_dict.json"), "w") as f:
            json.dump(processed_word_dictionary, f, indent=4)

    @staticmethod
    def _are_strings_diff_by_only_one_char(string1, string2):
        """
        Returns true if passed strings are different by only one character.

        :param string1: first string
        :param string2: second string to be checked against the first
        :return: bool
        """
        check = False
        for c1, c2 in zip(string1, string2):
            if c1 != c2:
                if check:
                    return False
                else:
                    check = True
        return check

    @staticmethod
    def _find_adjacent_words(word_arg, word_dict):
        """
        Finds all words from the passed word dict that are the same length with the passed word argument and that only
        differ by one character.

        :param word_arg: Word to be used as base for the adjacent words
        :param word_dict: Word dictionary containing all English words categorised by their length
        :return: list
        """
        return [word for word in word_dict[len(word_arg)]
                if WordLadder._are_strings_diff_by_only_one_char(word, word_arg)]

    def _find_next_branch(self, current_nodes, depth):
        """
        Finds the next branch of the ladder by finding all potential next nodes for each of the current nodes and
        checking whether they have been visited again. If not, it adds them to the next level node list.

        :param current_nodes: List of the current level nodes
        :param depth: Depth of the current level
        :return: list
        """
        self.word_ladder_dict[depth + 1] = list()
        for node in current_nodes:
            potential_next_nodes = self.word_dictionary[str(len(node))][node]
            for next_node in potential_next_nodes:
                if next_node not in self._nodes.keys():
                    self._nodes[str(next_node)] = Node(str(next_node), parent=self._nodes[str(node)])
                    self.word_ladder_dict[depth + 1].append(next_node)
        return self.word_ladder_dict[depth + 1]

    def find_shortest_word_ladder(self):
        """
        Finds the shortest word ladder between the starting and ending word, for which in every step only one of the
        letters of the starting word changes in order to become eventually the ending word.

        Prints the word ladder's branches and solution, along with information about it, while also returning the
        word ladder in string format.
        :return: str
        """
        # find the word ladders' branches
        self._nodes[str(self.starting_word)] = Node(self.starting_word)
        self.word_ladder_dict[0] = [self.starting_word]
        depth = 0
        potential_next_nodes = [self.starting_word]
        while self.ending_word not in potential_next_nodes:
            if not potential_next_nodes:
                raise Exception("No next nodes found. Problem unsolvable with dictionary provided.")
            print(f"Depth:{depth}, Nodes:{self.word_ladder_dict[depth]}")
            potential_next_nodes = self._find_next_branch(potential_next_nodes, depth)
            depth += 1
        self.word_ladder_dict[depth] = potential_next_nodes
        print(f"Depth:{depth}, Nodes:{potential_next_nodes}")

        # print out the word ladder and info
        solution_ladder_string = str(self._nodes[self.ending_word]).split("'")[1][1:].replace("/", " -> ")
        print(f"\nSolution ladder: {solution_ladder_string}")
        print(f"Steps required: {depth}")
        print(f"Nodes visited: {len(self._nodes)}")

        return solution_ladder_string

