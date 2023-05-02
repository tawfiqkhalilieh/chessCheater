import chess
import random

# TODO: analyze every opening manually

class Openings:

    def __init__(self) -> None:
        self.white_openings = {
            "Ruy López": [
                "e2e4",
                "e7e5",
                "g1f3",
                "b8c6",
                "f1b5",
                {
                    "Morphy Defence": [
                        "a7a6",
                        "b5a4",
                        {
                            "Closed Defence": [
                                "g8f6",
                                "e1g1",
                                "f8e7",
                                'f1e1'
                                "e8g8",
                                "c2c3",
                                "b7b5",
                                "a4b3",
                            ],
                            "Modern Steinitz Defence": ["d7d6"],
                            "Delayed Steinitz Defence": ["g8f6", "e1g1", "d7d6"],
                        },
                    ],
                    "Berlin Defence": ["g8f6"],
                    "Schliemann Defence": ["f7f5"],
                    "Classical Defence": ["f8c5"],
                },
            ],
            "Queen's Gambit": [
                "d2d4",
                "d7d5",
                "c2c4",
                {
                    "Queen's Gambit Accepted": ["d5c4"],
                    "Queen's Gambit Declined": ["e7e6"],
                    "Slav Defence": ["c7c6"],
                    "Albin Counter-Gambit": ["e7e5", "d4e5", "d5d4"]
                },
            ],
            "Italian Game": [
                "e2e4",
                "e7e5",
                "g1f3",
                "b8c6",
                "f1c4",
                {
                    "Hungarian Defence": ["f8e7"],
                    "Two Knights Defence": ["g8f6", 'd3', 'f8c5'],
                    "Giuoco Piano": ["f8c5"],
                    "Evans Gambit": ["f8c5", "b2b4"]
                },
            ],
            "Catalan Opening": [
                "d2d4",
                "g8f6",
                "c2c4",
                "e7e6",
                "g2g3",
                {
                    "Open Catalan": ["d7d5", "f1g2", "d5c4"],
                    "Closed Catalan": ["d7d5", "f1g2", "f8e7"],
                    "Modern Defence": ["d7d5", "f1g2", "c7c6"],
                    "Classical Defence": ["f8b4"],
                    "Bogo-Indian Defence": ["f8b4", "b1c3"]
                },
            ],
            "King's Indian Attack": [
                "e2e4",
                {
                    "King's Indian Attack": ["d2d3", "b1d2", "g1f3", "g2g3", "f1g2", "e1g1"]
                }
            ]
        }

        self.black_openings = {
            "French Defence": [
                "e2e4",
                "e7e6",
                "d2d4",
                "d7d5",
                {
                    "Advance Variation": ["e4e5"],
                    "Exchange Variation": ["e4d5"],
                    "Tarrasch Variation": ["g1f3"],
                    "Main line": ["b1c3"],
                    "Winawer Variation": ["b1c3", "f8b4"]
                },
            ],
            "Sicilian Defence": [
                "e2e4",
                "c7c5",
                {
                    "Najdorf Variation": ["g1f3", "d7d6", "d2d4", "c5d4", "f3d4", "g8f6", "b1c3", "a7a6"],
                    "Dragon Variation": ["g1f3", "d7d6", "d2d4", "c5d4", "f3d4", "g8f6", "b1c3", "g7g6"],
                    "Classical Variation": ["g1f3", "d7d6", "d2d4", "c5d4", "f3d4", "g8f6", "b1c3", "b8c6"],
                    "Scheveningen Variation": ["g1f3", "d7d6", "d2d4", "c5d4", "f3d4", "g8f6", "b1c3", "e7e6"],
                    "Sveshnikov Variation": ["g1f3", "b8c6", "d2d4", "c5d4", "f3d4", "g8f6", "b1c3", "e7e5"]
                },
            ],
            "Dutch Defence": [
                "d2d4",
                "f7f5",
                {
                    "Leningrad Variation": ["g2g3", "g7g6"],
                    "Classical Variation": ["g1f3", "e7e6"],
                    "Stonewall Variation": ["e2e3", "e7e6", "f1d3", "d7d5"]
                }
            ]
        }

    def get_move(self, board: chess.Board) -> chess.Move:
        # If the board is empty, pick a random opening
        if board.fullmove_number == 1:
            if board.turn == chess.WHITE:
                opening = random.choice(list(self.white_openings.keys()))
                moves = self.white_openings[opening]
            else:
                opening = random.choice(list(self.black_openings.keys()))
                moves = self.black_openings[opening]
            # Return the first move of the opening
            return chess.Move.from_uci(moves[0])
        
        # If the board is not empty, try to find a matching opening
        else:
            # Get the list of moves played so far
            history = [move.uci() for move in board.move_stack]
            # Loop through the openings dictionary
            if board.turn == chess.WHITE:
                openings = self.white_openings
            else:
                openings = self.black_openings
            for opening, moves in openings.items():
                # Check if the history matches the opening moves
                if history[:len(moves)] == moves[:len(history)]:
                    # If there is a next move in the opening, return it
                    if len(history) < len(moves):
                        return chess.Move.from_uci(moves[len(history)])
                    # If there is a branch in the opening, pick a random one and return its first move
                    elif isinstance(moves[-1], dict):
                        branch = random.choice(list(moves[-1].keys()))
                        return chess.Move.from_uci(moves[-1][branch][0])
        
        # If no move is found in the openings data, return None
        return None
    
openings_book = Openings()