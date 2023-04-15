
class Hand:
    def __init__(self, player_1=None):
        self.cards = []
        self.player = player_1
        self.team = player_1.team

    def draw(self, amount=1):
        cards = self.player.deck.get_card(amount)
        self.cards += cards

    def choose_card(self):
        index = self.player.interface.click_on_hand()
        return index

    def remove_card(self, index):
        self.cards.remove(self.cards[index])

    def return_card(self, index):
        self.player.deck.shuffle_card(self.cards[index])
        self.remove_card(index)
