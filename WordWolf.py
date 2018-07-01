from collections import Counter
from copy import deepcopy

with open('bookworm2.txt', 'r') as bookworm2:
    bookworm2_dict = bookworm2.read().split('\n')

board = ['a', 'b', 'c', 'd',
         'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p']

board = Counter(board)
wildcards = 0
if '*' in board:
    wildcards = board['*']

anagrams = []

for word in bookworm2_dict:
    cword = Counter(word)
    letters = cword.keys()
    if(letters <= board.keys()):
        new_board = deepcopy(board)
        for letter in letters:
            new_board[letter] -= cword[letter]
        if sum([val for val in new_board.values() if val < 0]) >= wildcards:
            anagrams.append(word)

anagrams = sorted(anagrams, key = lambda x: len(x), reverse = True)
with open('anagrams.txt', 'w') as out:
    out.write("\n".join(anagrams))
