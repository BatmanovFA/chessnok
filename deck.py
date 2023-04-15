import content
import random

class Deck:
    def __init__(self, player=None):
        self.deck = []
        self.team = player.team
        for name in content.DECK:
            self.deck.append(content.FIGURE_TYPES[name](team=self.team))

    def deck_is_empty(self):
        return len(self.deck) == 0

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self, amount=1):
        cards = []
        for i in range(amount):
            if self.deck_is_empty():
                break
            cards.append(self.deck.pop())
        return cards

    def shuffle_card(self, card_1):
        self.deck.append(card_1)
        self.shuffle()
