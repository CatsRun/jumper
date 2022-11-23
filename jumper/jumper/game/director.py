from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
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
        # new_location = self._terminal_service.read_number("\nEnter a location [1-1000]: ")
        # self._seeker.move_location(new_location)

        # self._puzzle_
        # self._guess_letter = "Guess a letter [a-z]: "

        self._puzzle._draw_word_selected()
        self._jumper.draw_jumper()
        self._letter_guessed = self._terminal_service.read_guess('Guess a letter [a-z]: ')
        
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        # self._hider.watch_seeker(self._seeker)
        # #replaces hint _ with guessed letter
        # if self._check_word(self._word) is True:
        #     self._index_guess = self._word.index(self._guess) #finds the index of _guess
        #     self._hint[self._index_guess] = self._guess #replaces _ with _guess

        # else:
        #     #remove parachute piece
        #     self._parachute.pop(0)

        
        # self._puzzle._check_guess()
        # self._puzzle._check_word()
        # self._puzzle._word_guess() #checks if all letters were guessed
        
        # self._puzzle._process_guess(self._letter_guessed)
        # self._puzzle._process_guess(self._letter_guessed)
        
        self._puzzle._process_guess(self._letter_guessed)

        if self._letter_guessed in self._puzzle._word_selected:
            self._jumper.draw_jumper()

        else:
            self._jumper.remove_chute_piece()

                

                
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        # hint = self._hider.get_hint()
        # self._terminal_service.write_text(hint)
        # if self._hider.is_found():
        #     self._is_playing = False

        #_draw_jumper
        #
        # self._puzzle._draw_word_selected()

        #end game
        # if self._jumper._parachute   #if len(_parachute[0]) > 1:

        
        if self._jumper.has_parachute() == False:
            self._jumper.parachute_gone()
            self._jumper.draw_jumper()
            self._is_playing = self._jumper.has_parachute()


        # if self._jumper.has_parachute() == False:
        #     self._jumper.parachute_gone()
        #     self._is_playing = False

        # elif self._puzzle.can_keep_guessing() == False:
        #     print('YAY, you own!')
        #     self._is_playing = False



   