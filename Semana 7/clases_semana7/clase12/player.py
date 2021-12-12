from abc import ABC, abstractmethod 

class Player(ABC):
    def __init__(self, name, can_play, major, position):
        self.name = name
        self.can_play = can_play
        self.major = major
        self.position = position
    
    @abstractmethod
    def play(self):
        pass
    
    
