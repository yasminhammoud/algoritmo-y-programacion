from player import Player

class Hitter(Player):
    def __init__(self, name, can_play, major, position, hits, turns, home_runs):
        super().__init__(name, can_play, major, position)
        self.hits = hits 
        self.turns = turns
        self.__home_runs = home_runs
    
    def play(self):
        print(f'{self.name} esta bateando')

    def get_home_runs(self):
        return self.__home_runs

h = Hitter('J', True, True, '1B', 1, 3, 0)
h.can_play
h.hits
h.major
h.
h.play()
