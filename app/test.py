import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_1_validate_rook_move(client):
    resp = client.get("/api/v1/rook/h1/h2")
    expected_result_test_1 = {
        "currentField": "H1",
        "destField": "H2",
        "error": None,
        "figure": "rook",
        "move": "valid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_1


def test_2_validate_queen_move(client):
    resp = client.get("/api/v1/queen/d1/h5")
    expected_result_test_2 = {
        "currentField": "D1",
        "destField": "H5",
        "error": None,
        "figure": "queen",
        "move": "valid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_2


def test_3_validate_queen_move_bad_field(client):
    resp = client.get("/api/v1/queen/d1/h55")
    expected_result_test_3 = {
        "currentField": "D1",
        "destField": "H55",
        "error": "Field does not exist.",
        "figure": "queen",
        "move": "invalid",
    }
    assert resp.status_code == 409
    assert resp.json == expected_result_test_3


def test_4_validate_move_bad_figure_name(client):
    resp = client.get("/api/v1/queegn/d1/h5")
    expected_result_test_4 = {
        "currentField": "D1",
        "destField": "H5",
        "error": "Piece does not exist.",
        "figure": "queegn",
        "move": "invalid",
    }
    assert resp.status_code == 404
    assert resp.json == expected_result_test_4


def test_5_validate_knight_move_invalid_move(client):
    resp = client.get("/api/v1/knight/a2/d3")
    expected_result_test_5 = {
        "currentField": "A2",
        "destField": "D3",
        "error": None,
        "figure": "knight",
        "move": "invalid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_5


def test_6_validate_knight_move(client):
    resp = client.get("/api/v1/knight/g4/f2")
    expected_result_test_6 = {
        "currentField": "G4",
        "destField": "F2",
        "error": None,
        "figure": "knight",
        "move": "valid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_6


def test_7_validate_king_move_invalid_move(client):
    resp = client.get("/api/v1/king/g4/f2")
    expected_result_test_7 = {
        "currentField": "G4",
        "destField": "F2",
        "error": None,
        "figure": "king",
        "move": "invalid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_7


def test_8_validate_king_move(client):
    resp = client.get("/api/v1/king/a1/b2")
    expected_result_test_8 = {
        "currentField": "A1",
        "destField": "B2",
        "error": None,
        "figure": "king",
        "move": "valid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_8


def test_9_validate_pawn_move_invalid_move(client):
    resp = client.get("/api/v1/pawn/d4/d6")
    expected_result_test_9 = {
        "currentField": "D4",
        "destField": "D6",
        "error": None,
        "figure": "pawn",
        "move": "invalid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_9


def test_10_validate_pawn_move(client):
    resp = client.get("/api/v1/pawn/d4/d5")
    expected_result_test_10 = {
        "currentField": "D4",
        "destField": "D5",
        "error": None,
        "figure": "pawn",
        "move": "valid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_10


def test_11_validate_bishop_move_invalid_move(client):
    resp = client.get("/api/v1/bishop/f3/g3")
    expected_result_test_11 = {
        "currentField": "F3",
        "destField": "G3",
        "error": None,
        "figure": "bishop",
        "move": "invalid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_11


def test_12_validate_bishop_move(client):
    resp = client.get("/api/v1/bishop/f3/h5")
    expected_result_test_12 = {
        "currentField": "F3",
        "destField": "H5",
        "error": None,
        "figure": "bishop",
        "move": "valid",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_12


def test_13_list_available_moves_rook(client):
    resp = client.get("/api/v1/rook/f3")
    expected_result_test_13 = {
        "availableMoves": [
            "F0",
            "F1",
            "F2",
            "F4",
            "F5",
            "F6",
            "F7",
            "F8",
            "A3",
            "B3",
            "C3",
            "D3",
            "E3",
            "G3",
            "H3",
        ],
        "currentField": "f3",
        "error": None,
        "figure": "rook",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_13


def test_14_list_available_moves_rook_bad_field(client):
    resp = client.get("/api/v1/rook/f9")
    expected_result_test_14 = {
        "availableMoves": [],
        "currentField": "f9",
        "error": "Field does not exist.",
        "figure": "rook",
    }
    assert resp.status_code == 409
    assert resp.json == expected_result_test_14


def test_15_list_available_moves_bad_figure_name(client):
    resp = client.get("/api/v1/que/c2")
    expected_result_test_15 = {
        "availableMoves": [],
        "currentField": "c2",
        "error": "Piece does not exist.",
        "figure": "que",
    }
    assert resp.status_code == 404
    assert resp.json == expected_result_test_15


def test_16_list_available_moves_bishop(client):
    resp = client.get("/api/v1/bishop/b1")
    expected_result_test_16 = {
        "availableMoves": ["C2", "A2", "D3", "E4", "F5", "G6", "H7"],
        "currentField": "b1",
        "error": None,
        "figure": "bishop",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_16


def test_17_list_available_moves_pawn(client):
    resp = client.get("/api/v1/pawn/h5")
    expected_result_test_17 = {
        "availableMoves": ["H6"],
        "currentField": "h5",
        "error": None,
        "figure": "pawn",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_17


def test_18_list_available_moves_queen(client):
    resp = client.get("/api/v1/queen/a8")
    expected_result_test_18 = {
        "availableMoves": [
            "B7",
            "C6",
            "D5",
            "E4",
            "F3",
            "G2",
            "H1",
            "A0",
            "A1",
            "A2",
            "A3",
            "A4",
            "A5",
            "A6",
            "A7",
            "B8",
            "C8",
            "D8",
            "E8",
            "F8",
            "G8",
            "H8",
        ],
        "currentField": "a8",
        "error": None,
        "figure": "queen",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_18


def test_19_list_available_moves_knight(client):
    resp = client.get("/api/v1/knight/d1")
    expected_result_test_19 = {
        "availableMoves": ["C3", "E3", "B2", "F2"],
        "currentField": "d1",
        "error": None,
        "figure": "knight",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_19


def test_20_list_available_moves_king(client):
    resp = client.get("/api/v1/king/f1")
    expected_result_test_20 = {
        "availableMoves": ["E1", "G1", "F2", "G2", "E2"],
        "currentField": "f1",
        "error": None,
        "figure": "king",
    }
    assert resp.status_code == 200
    assert resp.json == expected_result_test_20
