from flask import jsonify
from .misc import valid_piece, valid_positions
from .chess_moves import get_figure_object
from app import app


@app.route("/api/v1/<string:figure_name>/<string:position>", methods=["GET"])
def get_available_moves(figure_name, position):
    valid_position = valid_positions(position)
    if not valid_position:
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": "Field does not exist.",
                    "figure": f"{figure_name}",
                    "currentField": f"{position}",
                }
            ),
            409,
        )

    elif not valid_piece(figure_name):
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": "Piece does not exist.",
                    "figure": f"{figure_name}",
                    "currentField": f"{position}",
                }
            ),
            404,
        )
    else:
        number, letter = valid_position
        figure = get_figure_object(figure_name, (number, letter))
        figure_available_moves = figure.list_available_moves()
        return (
            jsonify(
                {
                    "availableMoves": figure_available_moves,
                    "error": None,
                    "figure": f"{figure_name}",
                    "currentField": f"{position}",
                }
            ),
            200,
        )


{
    "move": "invalid",
    "figure": "rook",
    "error": "Current move is not permitted.",
    "currentField": "H2",
}


@app.route(
    "/api/v1/<string:figure_name>/<string:position>/<string:next_position>",
    methods=["GET"],
)
def validate_move(figure_name, position, next_position):
    valid_position = valid_positions(position)
    valid_next_position = valid_positions(next_position)
    position = position.upper()
    next_position = next_position.upper()
    if not valid_position or not valid_next_position:
        return (
            jsonify(
                {
                    "move": "invalid",
                    "figure": f"{figure_name}",
                    "error": "Field does not exist.",
                    "currentField": f"{position}",
                    "destField": f"{next_position}",
                }
            ),
            409,
        )

    elif not valid_piece(figure_name):
        return (
            jsonify(
                {
                    "move": "invalid",
                    "figure": f"{figure_name}",
                    "error": "Piece does not exist.",
                    "currentField": f"{position}",
                    "destField": f"{next_position}",
                }
            ),
            404,
        )
    else:
        number, letter = valid_position
        figure = get_figure_object(figure_name, (number, letter))
        validate_move = figure.validate_move(next_position)
        return (
            jsonify(
                {
                    "move": f"{validate_move}",
                    "figure": f"{figure_name}",
                    "error": None,
                    "currentField": f"{position}",
                    "destField": f"{next_position}",
                }
            ),
            200,
        )


if __name__ == "__main__":
    app.run(debug=True)
