
class Interface:
    def __init__(self, player_1=None, field=None):
        self.player_1 = player_1
        self.field = field

    def click_on_hand(self, pos_x, pos_y):
        pass

    def click_on_field(self):
        pass

    def click_on_deck(self):
        pass

    def click_on_discard(self):
        pass
