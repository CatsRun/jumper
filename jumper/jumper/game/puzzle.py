import random
from game.terminal_service import TerminalService

class Puzzle:
    """Guess random word chosen from list.
    
    The responsibility of Puzzle is to create the puzzle to be solved.
    
    Attributes:            
        _puzzle_word (List[str]): List of words to guess from.
        _word_selected (str): Selected word from puzzle word list.
        _word_guess (List[str]): Display if underlines for each letter in word selected.
        _terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """

        self._puzzle_word = ['rome', 'paris', 'berlin', 'dubia']
        self._word_selected = self._puzzle_word[random.randint(0, len(self._puzzle_word)-1)] #how to pull a random word from a list
        self._word_guess = ['_'] * len(self._word_selected)
        self._terminal_service = TerminalService()
        

    def _draw_word_selected(self):
        """Draws _ for length of word guess. It is then printed by terminal services.

        Args:
            self (Puzzle): An instance of Puzzle.        
        """
        _guess = '' #local veriable to use in loop for appending word guess
        for space in self._word_guess:
            _guess += space #appends _ to itself
        self._terminal_service.write_text(_guess)


    def _process_guess(self, _letter_guessed):
        """Process the guess. If letter guessed is in the word return True

        Args: 
            self (Puzzle): An instance of Puzzle.
            _letter_guessed: User input for the letter guessed to solve the puzzle. 

        Return: 
            Boolian 
        """        
        _correct_guess = False #default response

        for i in range(0, len(self._word_selected)):
            if _letter_guessed == self._word_selected[i]:
                self._word_guess[i] = _letter_guessed
                _correct_guess = True 

        return _correct_guess


    def can_keep_guessing(self):
        """Should game continue based on guess word completed. Checks if the puzzle has been solved.

        Args: 
            self (Puzzle): An instance of Puzzle.

        Return: 
            Boolian 
        """ 

        return '_' in self._word_guess


    def _check_word(self):
        """Check to see if there are any more letters to guess.
        
        Args:
            self (Puzzle): An instance of Puzzle.                

        Return:
            Boolian
        """
        #This is the expanded form of what is in the return
        # if '_' in self._hint:
        #     return True
        # else:
        #     return False
        return '_' in self._word_guess
