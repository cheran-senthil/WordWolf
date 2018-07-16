"""WoldWolf Anagrammer"""

class Anagrammer:
    """Anagrammer class to support operations"""

    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    WILDCARDS = '*?'
    CHARECTERS = LETTERS + WILDCARDS

    with open('bookworm2.txt', 'r') as bookworm2:
        bookworm2_dict = bookworm2.read().split('\n')

    DICTIONARY = bookworm2_dict
    COUNTER_DICT = {}

    for word in DICTIONARY:
        word_dict = dict(zip(LETTERS, [0]*26))
        for letter in word:
            word_dict[letter] += 1
        COUNTER_DICT[word] = word_dict

    def __init__(self, letters):
        self.letters = list(letters)

    def search(self):
        """Search for subwords"""
        letters_dict = dict(zip(Anagrammer.CHARECTERS, [0]*28))
        for letter in self.letters:
            letters_dict[letter] += 1

        wildcards = 0
        wildcards += letters_dict.pop('*')
        wildcards += letters_dict.pop('?')

        sub_words = []

        for word, word_dict in Anagrammer.COUNTER_DICT.items():
            extra_letters = 0
            for letter in Anagrammer.LETTERS:
                letter_diff = word_dict[letter] - letters_dict[letter]
                if letter_diff > 0:
                    extra_letters += letter_diff
            if extra_letters <= wildcards:
                sub_words.append(word)

        return sub_words





# anagrams = []
#
# for word in bookworm2_dict:
#     cword = Counter(word)
#     letters = cword.keys()
#     if(letters <= board.keys()):
#         new_board = deepcopy(board)
#         for letter in letters:
#             new_board[letter] -= cword[letter]
#         if sum([val for val in new_board.values() if val < 0]) >= wildcards:
#             anagrams.append(word)
#
# anagrams = sorted(anagrams, key = lambda x: len(x), reverse = True)
# with open('anagrams.txt', 'w') as out:
#     out.write("\n".join(anagrams))
