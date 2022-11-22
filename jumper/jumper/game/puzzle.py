import random

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
        # self._location = random.randint(1, 1000)
        # self._distance = [0, 0] # start with two so get_hint always works

        self._puzzle_word = ['rome', 'paris', 'berlin', 'dubia']
        self._hint = '' #add _ for length._puzzle_word
        self._word = self._puzzle_word[random.randint(0, len(_puzzle_word)-1)] #how to pull a random word from a list
        self._check_guess = '' #this is user input. Should it be in a different class?
        self._check_word = len(self._puzzle_word) #is this right? does it pull what the signle word is?

    def _check_word(self):
        """Check to see if there are any more letters to guess
        
        Args:
            self                
        """


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
        if _guess in self._word:                  
            return True
        else:
            return False


    def _check_word(self):
        """Checks if the word is complete by checking the hint list for underscores. 
        
        Args:
            self

        Return: 
            True/False
        """
        #does hint[] have _ in it?


    

        


        


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


    