from player import Player

class Pitcher(Player):
    def __init__(self, name, can_play, major, position, pitches):
        super().__init__(name, can_play, major, position)
        self.pitches = pitches

    def play(self):
        print(f'{self.name} esta pichando')