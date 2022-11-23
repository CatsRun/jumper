from game.terminal_service import TerminalService

class Jumper:
    """Display for the person and parachute .
    
    The responsibility of Jumper it so create the display and determine then the parachute will be removed.
    
    Attributes:        
        _parachute (List[str]): display for parachute
        _jumper (List[str]): display for jumper
        _terminal_service: For getting and displaying information on the terminal.
    """    


    def __init__(self):        
        """Constructs a new Jumper.

        Args:
            self (Seeker): An instance of Jumper.
        """

        self._parachute = [' ___', '/___\ ', '\   /', ' \ /' ] #list for what will be dispayed as the parachute
        self._jumper = ['  O', ' /|\ ', ' / \ ', '', '^^^^^^^'  ] #list for what will be dispayed as the jumper
        self._terminal_service = TerminalService() #access to terminal services


    def draw_jumper(self):
        """Draws jumper and parachute using terminal services.

        Args:
            self (Seeker): An instance of Jumper.        
        """

        for i in self._parachute:
            self._terminal_service.write_text(i) #this draws the parachute

        for i in self._jumper:
            self._terminal_service.write_text(i) #this draws the jumper


    def remove_chute_piece(self):
        """Determines if a parachute piece should be removed. 
        
        Args:
            self (Seeker): An instance of Jumper

        Return: Boolian
        """
  
        self._parachute.pop(0) #removes first parachute piece

        #Note to self to add: change self._parachute.pop(1) and add "\n" as _parachute[1] to add a new line that will give a space between word guess and parachute.


    def has_parachute(self):
        """Checks if parachute is left. If length of parachute is 0, return True

        Args:
            self (Seeker): An instance of Jumper

        Return:
            Boolian
        
        """

        #checks if parachute is left, if none game ends
        if len(self._parachute) == 0:
            return False
        else:
            return True


    def parachute_gone(self):
        """Changes head of jumper from O to x when game ends due to no parachute left. 
        
        Args:
            self (Seeker): An instance of Jumper        

        """        
        self._jumper[0] = '  X'



