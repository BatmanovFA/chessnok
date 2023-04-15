

class Fight:
    def __init__(self, field=None, cell_d=None, figure_a=None, figure_d=None):
        self.field = field
        self.cell_d = cell_d
        self.figure_a = figure_a
        self.figure_d = figure_d
        self.strength_a = figure_a.strength
        self.strength_d = figure_d.strength

    def buff_figure(self):
        self.strength_a += self.figure_a.buff(1)
        self.strength_d += self.figure_d.buff(2)

    def check_can_we_attack(self):
        if self.strength_a < self.strength_d:
            return [0, 1]
        if self.strength_a == self.strength_d:
            return [0, 0]
        allowed_x = [1, 2]
        if self.field[allowed_x[self.figure_a.team - 1]][self.cell_d.coordinate_y] is None:
            return [1, 0]
        return [2, 1]
    def who_eat(self):
        pass
