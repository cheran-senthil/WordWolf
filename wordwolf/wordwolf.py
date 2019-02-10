"""WoldWolf Anagrammer"""


class Dictionary:
    """Dictionary class to support operations"""

    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    WILDCARDS = '*?'
    CHARECTERS = LETTERS + WILDCARDS

    def __init__(self, dictionary_file):
        with open(dictionary_file, 'r') as dictionary:
            self.dictionary = dictionary.read().split('\n')

        self.counter_dict = {}

        for word in self.dictionary:
            word_dict = dict(zip(Dictionary.LETTERS, [0] * 26))
            for letter in word:
                word_dict[letter] += 1
            self.counter_dict[word] = word_dict

    def search(self, letters, start='', end='', contains=''):
        """Search for subwords"""

        letters_dict = dict(zip(Dictionary.CHARECTERS, [0] * 28))
        for letter in letters:
            letters_dict[letter] += 1

        wildcards = 0
        wildcards += letters_dict.pop('*')
        wildcards += letters_dict.pop('?')

        sub_words = []

        for word, word_dict in self.counter_dict.items():
            if word.startswith(start) and word.endswith(end) and (
                    contains in word):
                wildcards_required = 0
                for letter in Dictionary.LETTERS:
                    extra_letters = word_dict[letter] - letters_dict[letter]
                    if extra_letters > 0:
                        wildcards_required += extra_letters
                if wildcards_required <= wildcards:
                    sub_words.append(word)

        return sub_words.sort(key=len)
