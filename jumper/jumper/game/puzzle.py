import random
from game.terminal_service import TerminalService

class Puzzle:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """

        self._puzzle_word = ['rome', 'paris', 'berlin', 'dubia']
        self._word_selected = self._puzzle_word[random.randint(0, len(self._puzzle_word)-1)] #how to pull a random word from a list
        # self._word_guess = ['_'] * len(self._word_selected)
        self._word_guess = ['_']  

        self._check_guess = '' #this is user input. Should it be in a different class?
        self._check_word = len(self._puzzle_word) #is this right? does it pull what the signle word is?
        self._terminal_service = TerminalService()
        
        #how do I get the index if I don't know the letter in puzzle?

        self._index_guess = self._word_selected.index(self._word_selected)
        


    # def _draw_word_selected(self):
    #     for i in self._word_guess:
    #         self._terminal_service.write_text(i)

    # draws an _ for each letter in _word_selected based on the index length
    def _draw_word_selected(self):
        for i in self._word_guess:
            i += '_' * (len(self._word_selected) -1)
            self._terminal_service.write_text(i)

            # ***********remove before 
            print(self._word_selected)
    


    def _process_guess(self, _letter_guessed):
        correct_guess = False
        # loop through word seleceted
        # for self._guess in self._word_selected:
        # # check if guess letter = word_seleted[index]
        #     if self._word_guess == self._word_selected[self._index_guess]:
        # # set _wordguess[index] = guess_letter
        #         self._word_guess[self._index_guess] = self._guess
        # return correct_guess

        # ******* this didnt work. out of range
        # for i in range(0, len(self._word_selected)):
        #     if _guess_letter in self._word_selected:
        #         self._word_guess[i]

        # find i in _word_guess
        self._word_guess[self._index_guess] = _letter_guessed
        return correct_guess




#************check this, was added off the other
    def can_keep_guessing(self):
        return '_' in self._word_guess






    def _check_word(self):
        """Check to see if there are any more letters to guess
        
        Args:
            self                
        """
        # if '_' in self._hint:
        #     return True
        # else:
        #     return False
        return '_' in self._word_guess

        



    def _check_guess(self):
        """Process the guess. If letter guessed is in the word return True
        
        Args:
            self

        Return: 
            True/False
        """
        #if True, letter (guess) needs to be added to hint by 
        # finding the index of the letter in _puzzle_word and replacing it into the matching index of the hint
        # put this in director?


        #this checks if _guess in is _word, return True
        if self._guess in self._word_selected:                  
            return True
        else:
            return False



    # def _check_word(self):
    #     """Checks if the word is complete by checking the hint list for underscores. 
        
    #     Args:
    #         self

    #     Return: 
    #         True/False
    #     """
    #     #does hint[] have _ in it?


    

        


        


    # def get_hint(self):
    #     """Gets a hint for the seeker.

    #     Args:
    #         self (Hider): An instance of Hider.
        
    #     Returns:
    #         string: A hint for the seeker.
    #     """
    #     hint = "(-.-) Nap time."
    #     if self._distance[-1] == 0:
    #         hint = "(;.;) You found me!"
    #     elif self._distance[-1] > self._distance[-2]:
    #         hint = "(^.^) Getting colder!"
    #     elif self._distance[-1] < self._distance[-2]:
    #         hint = "(>.<) Getting warmer!"
    #     return hint

    # def is_found(self):
    #     """Whether or not the hider has been found.

    #     Args:
    #         self (Hider): An instance of Hider.
            
    #     Returns:
    #         boolean: True if the hider was found; false if otherwise.
    #     """
    #     return (self._distance[-1] == 0)
        
    # def watch_seeker(self, seeker):
    #     """Watches the seeker by keeping track of how far away it is.

    #     Args:
    #         self (Hider): An instance of Hider.
    #     """
    #     distance = abs(self._location - seeker.get_location())
    #     self._distance.append(distance)


    