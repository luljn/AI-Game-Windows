# Game status enum.
from enum import StrEnum



class GameStatus(StrEnum) :
    
    phase_1 = "put pawns on board"
    phase_2 = "deplacement"