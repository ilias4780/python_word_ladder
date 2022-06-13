from anytree import Node, RenderTree


class WordLadder:
    """
    Word ladder class that finds all possible, but also most efficient word path between a starting and an ending
    english word, when supplied with a list of english words.

    :param word_list: List of english words (words should all be lowercase and not contain symbols or spaces)
    """

    def __init__(self, word_list: list):
        self.word_list = word_list

        # create placeholders
        self._ending_word = None
        self._starting_word = None
        self._word_dictionary = dict()
        self.word_ladder_dict = dict()
        self._nodes = dict()

        # process the word list
        self._process_word_list()

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
        if new_starting_word in self.word_list:
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
        elif new_ending_word not in self.word_list:
            raise Exception("Please enter a valid ending word.")
        else:
            self._ending_word = new_ending_word

    def _process_word_list(self):
        """
        Processes the passed word list into a word dictionary, with keys the length of words and values the words with
        such length.
        """
        for word in self.word_list:
            if len(word) not in self._word_dictionary:
                self._word_dictionary[len(word)] = [word, ]
            else:
                self._word_dictionary[len(word)].append(word)

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
    def _count_character_differences_in_strings(string1, string2):
        """
        Returns the number of character differences between two strings.

        :param string1: first string
        :param string2: second string to be checked against the first
        :return: int
        """
        count = 0
        for c1, c2 in zip(string1, string2):
            if c1 != c2:
                count += 1
        return count

    def _find_adjacent_words(self, word_arg):
        """
        Finds all words from the used word list that are the same length with the passed word argument and that only
        differ by one character.

        :param word_arg: Word to be used as base for the adjacent words
        :return: list
        """
        return [word for word in self._word_dictionary[len(word_arg)]
                if self._are_strings_diff_by_only_one_char(word, word_arg)]

    def _find_potential_next_nodes(self, working_word):
        """
        Finds all potential next nodes for the passed word. All potential next nodes are valid english words that
        differ from the passed word by one character and are more similar to the end word than the passed one.

        :param working_word: Word to be used as base for the potential next nodes
        :return: list
        """
        potential_next_nodes = list()
        char_differences = self._count_character_differences_in_strings(working_word, self.ending_word)
        adjacent_words = self._find_adjacent_words(working_word)
        for word in adjacent_words:
            if self._count_character_differences_in_strings(word, self.ending_word) < char_differences:
                potential_next_nodes.append(word)
        return potential_next_nodes

    def _find_word_ladders(self, word):
        """
        Finds all the possible word ladders between then passed word and the ending word, in a recurring fashion.

        :param word: Word to be used in the search for the ladder
        :return: list
        """
        self.word_ladder_dict[word] = list()
        potential_next_nodes = self._find_potential_next_nodes(word)
        for node in potential_next_nodes:
            self._nodes[str(node)] = Node(str(node), parent=self._nodes[str(word)])
            self.word_ladder_dict[word].append(node)
            if node == self.ending_word:
                return
            else:
                self._find_word_ladders(node)

    def return_word_ladders(self):
        """
        Finds all possible word ladders between the starting and ending word, for which in every step only one of the
        letters of the starting word changes in order to become eventually the ending word.
        :return: list of lists
        """

        # find all the possible word ladders
        self._nodes[str(self.starting_word)] = Node(str(self.starting_word))
        self._find_word_ladders(self.starting_word)

        # print out the word ladders tree
        for pre, fill, node in RenderTree(self._nodes[str(self.starting_word)]):
            print("%s%s" % (pre, node.name))

        return self.word_ladder_dict

