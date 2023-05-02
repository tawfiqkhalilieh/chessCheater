import chess.svg

def render_board(chess_board, game_number):
    with open(f"games/game-{game_number}.svg", 'w') as file:
            if chess.svg.board:
                file.write(chess.svg.board(
                    chess_board,
                    size=1000,
                ))