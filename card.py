

class Card:
    def __init__(self, strength=None, card_type=None, team=None, cell_1=None, player_1=None):
        self.strength = strength
        self.card_type = card_type
        self.team = team
        self.cell = cell_1
        self.player = player_1

    def on_play(self):
        pass

    def buff(self, typ):
        pass


class Pawn(Card):
    def __init__(self):
        super().__init__(1, "Pawn")

    def on_play(self):
        self.player.hand.draw(1)


class Knight(Card):
    def __init__(self):
        super().__init__(2, "Knight")

    def buff(self, typ):
        if typ == 1:
            return 1


class Bishop(Card):
    def __init__(self):
        super().__init__(2, "Bishop")

    def buff(self, typ):
        if typ == 2:
            return 1


class Rook(Card):
    def __init__(self):
        super().__init__(3, "Rook")

    def buff(self, typ):
        allowed_pos = [0, 3]
        if self.cell.coordinate_x == allowed_pos[self.team - 1]:
            return 1


class Queen(Card):
    def __init__(self):
        super().__init__(4, "Queen")


class King(Card):
    def __init__(self):
        super().__init__(3, "King")
