from hand import Hand
from deck import Deck
from interface_chessnok import Interface


class Player:
    def __init__(self, team=None, game=None):
        self.team = team
        self.deck = Deck(self)
        self.hand = Hand(self)
        self.interface = Interface(self)
        self.game = game

    def play_card(self, card, cell, index):
        self.game.field[cell.coordinate_x][cell.coordinate_y].card = card
        self.hand.remove_card(index)

    def move_card(self, cell_1, cell_2):
        self.game.field.move_figure(cell_1, cell_2)

    def attack_card(self):
        pass

    def choose_card_hand(self):
        pass

    def choose_card_field(self):
        pass
