import random
#Angela Murray
#Jumper practice file

#This is the basice outline for the jumper game. There is no loop because it will be in the other file.
# It is missing other pieces such as classes and methods... these will be added in the other file. 

#What is here: list of word, chosen word, parachute and jumper display, user input, 
# check user input against chosen word with if else, add guess to hint or remove chute piece, 
# reprint of changed chute or hint. 

_parachute = [' ___', '/___\ ', '\   /', ' \ /' ]
_jumper = ['  O', ' /|\ ', ' / \ ', '', '^^^^^^^'  ]

#loop to print parachute
for i in _parachute:
    print(f'{i}')

# loop to print _jumper
for i in _jumper:
    print(i)

_puzzle_word = ['rome', 'paris', 'berlin', 'dubia'] #list of random words
_word = _puzzle_word[random.randint(0, len(_puzzle_word)-1)] #how to pull a random word from a list
print(_word) #print _word to help test
_hint = [] #this must be a list

#print hint, _ for each letter in _puzzle_word
for i in _word: 
    _hint += ('_')

print(*_hint) #adding * makes the formatting change to just the letters and on the same line

_guess = input('Guess a letter [a-z]: ') #asking for user input, guess



def _check_word(_word):
#this checks if _guess in is _word, return True
    if _guess in _word:                  
        return True
    else:
        return False


_check_word(_word) #calls method



#replaces hint _ with guessed letter
if _check_word(_word) is True:
    _index_guess = _word.index(_guess) #finds the index of _guess
    _hint[_index_guess] = _guess #replaces _ with _guess

else:
    #remove parachute piece
    _parachute.pop(0)
    

# reprint(_parachute) with removed piece
for i in _parachute:
    print(f'{i}')


# reprint _hint with prpper formating after _guess
print(*_hint)