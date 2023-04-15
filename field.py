from cell import Cell
from card import Card


class Field:
    def __init__(self):
        self.field = []
        for i in range(4):
            field = []
            for j in range(4):
                team = 2
                if i < 2:
                    team = 1
                field.append(Cell(coordinate_x=i, coordinate_y=j, team=team))
            self.field.append(field)

    def cell_inform(self, cell_1):
        return self.field[cell_1.coordinate_x][cell_1.coordinate_y].card.card_type

    def choose_cell_to_move(self, cell_1, team):
        cells_m = []
        cells_a = []
        if cell_1.card.card_type == "Pawn":
            cells_m = self.pawn_choose_move(cell_1, team)
            cells_a = self.pawn_choose_attack(cell_1, team)
        if cell_1.card.card_type == "Knight":
            cells_m = self.knight_choose_move(cell_1, team)
            cells_a = self.knight_choose_attack(cell_1, team)
        if cell_1.card.card_type == "Bishop":
            cells_m = self.bishop_choose_move(cell_1, team)
            cells_a = self.bishop_choose_attack(cell_1, team)
        if cell_1.card.card_type == "Rook":
            cells_m = self.rook_choose_move(cell_1, team)
            cells_a = self.rook_choose_attack(cell_1, team)
        if cell_1.card.card_type == "Queen":
            cells_m = self.queen_choose_move(cell_1, team)
            cells_a = self.queen_choose_attack(cell_1, team)
        return [cells_m, cells_a]

    def remove_figure(self, cell_1):
        self.field[cell_1.coordinate_x][cell_1.coordinate_y].card = Card()

    def choose_cell_to_play(self, team):
        cells = []
        for i in [0, 1, 2, 3]:
            for j in [0, 1]:
                pos_x = j
                if team == 2:
                    pos_x += 2
                if self.field[j][i].card.card_type is None:
                    cells.append(self.field[j][i])
        return cells

    def move_figure(self, cell_1, cell_2):
        self.field[cell_1.coordinate_x][cell_1.coordinate_y].card = cell_2.card
        self.field[cell_2.coordinate_x][cell_2.coordinate_y].card = Card()

    def pawn_choose_move(self, cell_1, team):
        cells = []
        if team == 1:
            if (cell_1.coordinate_x + 1 < 2 and
                    self.field[cell_1.coordinate_x + 1][cell_1.coordinate_y].is_empty()):
                cells.append(self.field[cell_1.coordinate_x + 1][cell_1.coordinate_y])
        if team == 2:
            if (cell_1.coordinate_x - 1 > 1 and
                    self.field[cell_1.coordinate_x - 1][cell_1.coordinate_y].is_empty()):
                cells.append(self.field[cell_1.coordinate_x - 1][cell_1.coordinate_y])
        return cells

    def knight_choose_move(self, cell_1, team):
        cells = []
        if team == 1:
            for i in [-1, 1]:
                for j in [-2, 2]:
                    if (-1 < cell_1.coordinate_x + i < 2 and
                            -1 < cell_1.coordinate_y + j < 4 and
                            self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j].is_empty()):
                        cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j])
            for i in [-2, 2]:
                for j in [-1, 1]:
                    if (-1 < cell_1.coordinate_x + i < 2 and
                            -1 < cell_1.coordinate_y + j < 4 and
                            self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j].is_empty()):
                        cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j])
        if team == 2:
            for i in [-1, 1]:
                for j in [-2, 2]:
                    if (1 < cell_1.coordinate_x + i < 4 and
                            -1 < cell_1.coordinate_y + j < 4 and
                            self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j].is_empty()):
                        cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j])
            for i in [-2, 2]:
                for j in [-1, 1]:
                    if (1 < cell_1.coordinate_x + i < 4 and
                            -1 < cell_1.coordinate_y + j < 4 and
                            self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j].is_empty()):
                        cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j])
        return cells

    def bishop_choose_move(self, cell_1, team):
        cells = []
        if team == 1:
            for i in [-1, 1]:
                for j in [-1, 1]:
                    if (-1 < cell_1.coordinate_x + i < 2 and
                            -1 < cell_1.coordinate_y + j < 4 and
                            self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j].is_empty()):
                        cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j])
        if team == 2:
            for i in [-1, 1]:
                for j in [-1, 1]:
                    if (1 < cell_1.coordinate_x + i < 4 and
                            -1 < cell_1.coordinate_y + j < 4 and
                            self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j].is_empty()):
                        cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + j])
        return cells

    def rook_choose_move(self, cell_1, team):
        cells = []
        if team == 1:
            for i in [-1, 1]:
                if (-1 < cell_1.coordinate_x + i < 2 and
                        -1 < cell_1.coordinate_y < 4 and
                        self.field[cell_1.coordinate_x + i][cell_1.coordinate_y].is_empty()):
                    cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y])
            for i in [1, 2, 3]:
                if -1 < cell_1.coordinate_x < 2 and -1 < cell_1.coordinate_y + i < 4:
                    if self.field[cell_1.coordinate_x][cell_1.coordinate_y + i].is_empty():
                        cells.append(self.field[cell_1.coordinate_x][cell_1.coordinate_y + i])
                    else:
                        break
            for i in [-1, -2, -3]:
                if -1 < cell_1.coordinate_x < 2 and -1 < cell_1.coordinate_y + i < 4:
                    if self.field[cell_1.coordinate_x][cell_1.coordinate_y + i].is_empty():
                        cells.append(self.field[cell_1.coordinate_x][cell_1.coordinate_y + i])
                    else:
                        break
        if team == 2:
            for i in [-1, 1]:
                if (1 < cell_1.coordinate_x + i < 4 and
                        -1 < cell_1.coordinate_y < 4 and
                        self.field[cell_1.coordinate_x + i][cell_1.coordinate_y].is_empty()):
                    cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y])
            for i in [1, 2, 3]:
                if 1 < cell_1.coordinate_x < 4 and -1 < cell_1.coordinate_y + i < 4:
                    if self.field[cell_1.coordinate_x][cell_1.coordinate_y + i].is_empty():
                        cells.append(self.field[cell_1.coordinate_x][cell_1.coordinate_y + i])
                    else:
                        break
            for i in [-1, -2, -3]:
                if 1 < cell_1.coordinate_x < 4 and -1 < cell_1.coordinate_y + i < 4:
                    if self.field[cell_1.coordinate_x][cell_1.coordinate_y + i].is_empty():
                        cells.append(self.field[cell_1.coordinate_x][cell_1.coordinate_y + i])
                    else:
                        break
        return cells

    def queen_choose_move(self, cell_1, team):
        cells = []
        cells += self.bishop_choose_move(cell_1, team)
        cells += self.rook_choose_move(cell_1, team)
        return cells

    def pawn_choose_attack(self, cell_1, team):
        cells = []
        if team == 1:
            for i in [-1, 1]:
                if (1 < cell_1.coordinate_x + 1 < 4 and
                        -1 < cell_1.coordinate_y + i < 4 and
                        not self.field[cell_1.coordinate_x + 1][cell_1.coordinate_y + i].is_empty()):
                    cells.append(self.field[cell_1.coordinate_x + 1][cell_1.coordinate_y + i])
        if team == 2:
            for i in [-1, 1]:
                if (-1 < cell_1.coordinate_x - 1 < 2 and
                        -1 < cell_1.coordinate_y + i < 4 and
                        not self.field[cell_1.coordinate_x - 1][cell_1.coordinate_y + i].is_empty()):
                    cells.append(self.field[cell_1.coordinate_x - 1][cell_1.coordinate_y + i])
        return cells

    def knight_choose_attack(self, cell_1, team):
        cells = []
        if team == 1:
            cells = self.knight_choose_move(cell_1, team=2)
        if team == 2:
            cells = self.knight_choose_move(cell_1, team=1)
        return cells

    def bishop_choose_attack(self, cell_1, team):
        cells = []
        if team == 1:
            for i in [1, 2, 3]:
                if (-1 < cell_1.coordinate_x + i < 4 and
                        -1 < cell_1.coordinate_y + i < 4 and
                        not self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + i].is_empty()):
                    if -1 < cell_1.coordinate_x + i < 2:
                        break
                    cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y + i])
                    break
                if (-1 < cell_1.coordinate_x + i < 4 and
                        -1 < cell_1.coordinate_y - i < 4 and
                        not self.field[cell_1.coordinate_x + i][cell_1.coordinate_y - i].is_empty()):
                    if -1 < cell_1.coordinate_x + i < 2:
                        break
                    cells.append([cell_1.coordinate_x + i, cell_1.coordinate_y - i])
                    break
        if team == 2:
            for i in [1, 2, 3]:
                if (-1 < cell_1.coordinate_x - i < 4 and
                        -1 < cell_1.coordinate_y + i < 4 and
                        not self.field[cell_1.coordinate_x - i][cell_1.coordinate_y + i].is_empty()):
                    if 1 < cell_1.coordinate_x - i < 4:
                        break
                    cells.append(self.field[cell_1.coordinate_x - i][cell_1.coordinate_y + i])
                    break
                if (-1 < cell_1.coordinate_x - i < 4 and
                        -1 < cell_1.coordinate_y - i < 4 and
                        not self.field[cell_1.coordinate_x - i][cell_1.coordinate_y - i].is_empty()):
                    if 1 < cell_1.coordinate_x - i < 4:
                        break
                    cells.append([cell_1.coordinate_x - i, cell_1.coordinate_y - i])
                    break
        return cells

    def rook_choose_attack(self, cell_1, team):
        cells = []
        if team == 1:
            for i in [1, 2, 3]:
                if (-1 < cell_1.coordinate_x + i < 4 and
                        not self.field[cell_1.coordinate_x + i][cell_1.coordinate_y].is_empty()):
                    if -1 < cell_1.coordinate_x + i < 2:
                        break
                    cells.append(self.field[cell_1.coordinate_x + i][cell_1.coordinate_y])
                    break
        if team == 2:
            for i in [1, 2, 3]:
                if (-1 < cell_1.coordinate_x - i < 4 and
                        not self.field[cell_1.coordinate_x - i][cell_1.coordinate_y].is_empty()):
                    if 1 < cell_1.coordinate_x - i < 4:
                        break
                    cells.append(self.field[cell_1.coordinate_x - i][cell_1.coordinate_y])
                    break
        return cells

    def queen_choose_attack(self, cell_1, team):
        cells = []
        cells += self.rook_choose_attack(cell_1, team)
        cells += self.bishop_choose_attack(cell_1, team)
        return cells

    def multy_attack_choose_figure(self, cell_1, team):
        pass
