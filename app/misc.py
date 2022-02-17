import re

from flask import abort


def valid_piece(figure_name: str) -> bool:
    pieces = ["rook", "bishop", "pawn", "queen", "knight", "king"]
    try:
        if figure_name.lower() in pieces:
            return True
        else:
            return False
    except Exception as e:
        print(
            f"An exception {e} was thrown during the execution\
                of a valid_piece function"
        )
        abort(404)


def valid_positions(position: str):
    try:
        letter = position[0]
        number = position[1:]
        if letter.isalpha() and number.isdigit():
            letter = letter.upper()
            number = int(number)
            if len(letter) == 1 and number in range(9) and re.match("[A-H]", letter):
                return number, letter
        return None
    except Exception as e:
        print(
            f"An exception {e} was thrown during the execution of a \
                valid_positions function"
        )
        abort(409)
