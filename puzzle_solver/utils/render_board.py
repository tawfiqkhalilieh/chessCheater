import chess.svg

def render_board(chess_board):
    with open("puzzle_solver/games/chess.svg", 'w') as file:
            if chess.svg.board:
                file.write(chess.svg.board(
                    chess_board,
                    size=1000,
                ))