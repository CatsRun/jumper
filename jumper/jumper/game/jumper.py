from game.terminal_service import TerminalService

# 1) Add the class declaration. Use the following class comment.
class Jumper:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """
    

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):        
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._location = 0  
        self._parachute = [' ___', '/___\ ', '\   /', ' \ /' ]
        self._jumper = ['  O', ' /|\ ', ' / \ ', '', '^^^^^^^'  ]
        self._terminal_service = TerminalService()

    def draw_jumper(self):
        for i in self._parachute:
            # print(f'{i}')
            self._terminal_service.write_text(i) #this draws the parachute
        for i in self._jumper:
            self._terminal_service.write_text(i)

    def remove_chute_piece(self):
        #remove parachute piece
        self._parachute.pop(0)

    def has_parachute(self):
        #checks if parachute is left, if none game ends
        if len(self._parachute) > 0:
            return False
        else:
            return True

    def parachute_gone(self):
        #changes head of jumper from O to x when game ends due to no parachute left. 
        return self._jumper[0].replace('O', 'X') #how does it know when to run this part?



#     def get_location(self):
#         """Gets the current location.
        
#         Returns  :
#             number: The current location,
#         """
#         return self._location


# # 4) Create the move_location(self, location) method. Use the following method comment.
#     def move_location(self, location):
#         """Moves to the given location.

#         Args:
#             self (Seeker): An instance of Seeker.
#             location (int): The given location.
#         """
#         self._location = location
        