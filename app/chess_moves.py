from abc import ABC, abstractmethod


class Figure(ABC):
    latters = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def __init__(self, position: tuple):
        self.position = position

    @abstractmethod
    def list_available_moves():
        pass

    def validate_move(self, get_to: str) -> str:
        list_available_moves = self.list_available_moves()
        if list_available_moves:
            print(get_to)
            if get_to in list_available_moves:
                return "valid"
        return "invalid"


class Rook(Figure):
    def __init__(self, position: tuple):
        super().__init__(position)

    def list_available_moves(self):
        position = self.position
        validate_move_l = []
        for number in range(9):
            if number != position[0]:
                validate_move_l.append(position[1] + str(number))
        for letter in self.latters:
            if letter != position[1]:
                validate_move_l.append(letter + str(position[0]))
        return validate_move_l


class Bishop(Figure):
    def __init__(self, position: tuple):
        super().__init__(position)

    def list_available_moves(self):
        position = self.position
        validate_move_l = []
        latters = self.latters
        index = latters.index(position[1])
        index_up = index
        index_down = index
        number_up = position[0]
        number_down = position[0]

        for i in range(7):
            index_up += 1
            number_up += 1
            index_down -= 1
            number_down -= 1

            if index_up <= 7 and number_up <= 8:
                validate_move_l.append(latters[index_up] + str(number_up))

            if index_down >= 0 and number_down >= 1:
                validate_move_l.append(latters[index_down] + str(number_down))

            if index_down >= 0 and number_up <= 8:
                validate_move_l.append(latters[index_down] + str(number_up))

            if index_up <= 7 and number_down >= 1:
                validate_move_l.append(latters[index_up] + str(number_down))

        return validate_move_l


def format_moves():
    pass


class Pawn(Figure):
    def __init__(self, position: tuple ):
        super().__init__(position)

    def list_available_moves(self):
        position = self.position
        validate_move_l = []
        if position[0] != 8:
            validate_move_l.append(position[1] + str(position[0] + 1))
        return validate_move_l


class Queen(Rook, Bishop):
    def __init__(self, position: tuple):
        super().__init__(position)

    def list_available_moves(self):
        return [*Bishop.list_available_moves(self), *Rook.list_available_moves(self)]


def get_moves_from_list(deltas: list, position: tuple, latters: list) -> list:
    index = latters.index(position[1])
    number = position[0]
    validate_move_l = []
    for (x, y) in deltas:
        xCandidate = number + x
        yCandidate = index + y
        if 1 <= xCandidate <= 8 and 0 <= yCandidate <= 7:
            validate_move_l.append(latters[yCandidate] + str(xCandidate))

    return validate_move_l


class Knight(Figure):
    def __init__(self, position: tuple):
        super().__init__(position)

    def list_available_moves(self):
        deltas = [
            (-2, -1),
            (-2, +1),
            (+2, -1),
            (+2, +1),
            (-1, -2),
            (-1, +2),
            (+1, -2),
            (+1, +2),
        ]
        position = self.position
        latters = self.latters
        return get_moves_from_list(deltas, position, latters)


class King(Figure):
    def __init__(self, position: tuple):
        super().__init__(position)

    def list_available_moves(self):
        deltas = [
            (0, -1),
            (0, +1),
            (+1, 0),
            (-1, 0),
            (+1, +1),
            (+1, -1),
            (-1, -1),
            (-1, +1),
        ]
        position = self.position
        latters = self.latters
        return get_moves_from_list(deltas, position, latters)


def get_figure_object(figure_name: str, position: tuple) -> object:
    figure_class_list = {
        "rook": Rook,
        "bishop": Bishop,
        "pawn": Pawn,
        "queen": Queen,
        "knight": Knight,
        "king": King,
    }
    figure_object = figure_class_list[figure_name](position)
    return figure_object
