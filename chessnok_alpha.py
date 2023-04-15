from field import Field
from player import Player


class ChessnokAlpha:
    def __init__(self):
        self.field = Field()
        self.player_1 = Player(1, self)
        self.player_2 = Player(2, self)

    def start_game(self):
        pass

    def start_turn(self, player):
        pass

    def end_turn(self, player):
        pass

    def end_game(self):
        pass
