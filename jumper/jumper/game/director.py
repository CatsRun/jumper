from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        self._puzzle: For getting puzzle information from Puzzle class 
        is_playing (boolean): Whether or not to keep playing.
        self._jumper: For getting jumper information from Jumper class 
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
                
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            self._get_inputs()
            self._do_updates() 
            self._do_outputs()


    def _get_inputs(self):
        """Gets guess of letter in word
        
        Args:
            self (Director): An instance of Director.
                    
        """

        self._puzzle._draw_word_selected() #draws the puzzle to solve
        self._jumper.draw_jumper() #draws the jumper with parachute
        self._letter_guessed = self._terminal_service.read_guess('Guess a letter [a-z]: ') #gets user input to solve puzzle
                
        
    def _do_updates(self):
        """Processes user input to change display of jumper and puzzle

        Args:
            self (Director): An instance of Director.
        """

        if self._puzzle._process_guess(self._letter_guessed) == False:
            self._jumper.remove_chute_piece() #remove piece of parachute



                
    def _do_outputs(self):
        """Displays end of game based on completing the puzzle or parachute is gone. 

        Args:
            self (Director): An instance of Director.
            
        """

        #ends game if parachute is gone
        if self._jumper.has_parachute() == False:
            self._jumper.parachute_gone()
            self._jumper.draw_jumper()
            self._terminal_service.write_text(f"Sorry, you didn't make it to {self._puzzle._word_selected.capitalize()}!")
            self._is_playing = self._jumper.has_parachute()

        #end game if puzzle is solved
        elif self._puzzle.can_keep_guessing() == False:            
            self._terminal_service.write_text(f'YAY, you landed in {self._puzzle._word_selected.capitalize()}!')
            self._is_playing = False



   