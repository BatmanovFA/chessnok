from card import Card


class Cell:
    def __init__(self, coordinate_x=None, coordinate_y=None, team=None):
        self.card = Card()
        self.team = team
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def is_empty(self):
        return self.card.card_type is None
