import chess
import chess.engine
import chess.svg
from automation.utils.render_board import render_board
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from puzzle_solver.utils.fetch_game import fetch_game
import asyncio
import time
from automation.utils.move import move as chess_move
from automation.utils.get_last_move import get_last_move

chess_board: chess.Board = chess.Board(fen='8/8/8/8/8/8/8/8 w - - 0 1', chess960=True)

# setup and configure the engine
engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")

PLAYER_COLOR = 'white'

options = Options()
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# navigate to a webpage
driver.get("https://www.chess.com/play/computer")
actions = ActionChains(driver)

time.sleep(20)

loop = asyncio.get_event_loop()
chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))

moves = 0

if PLAYER_COLOR == 'white':
    result = engine.play(chess_board, chess.engine.Limit(time=0.1)).move
    print(result)
    chess_board.push(result)
    moves += 1
    chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as=PLAYER_COLOR)
    render_board(chess_board=chess_board, game_number="chess960")

while not chess_board.is_game_over():
    try:

        last_move = get_last_move(driver=driver,turn= "white" if PLAYER_COLOR == "black" else "black")
        while not last_move:
            last_move = get_last_move(driver=driver,turn= "white" if PLAYER_COLOR == "black" else "black")
        try:
            chess_board.push_san(last_move)
        except:
            chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))

        if ( chess_board.turn == chess.BLACK and PLAYER_COLOR == 'black') or ( chess_board.turn == chess.WHITE and PLAYER_COLOR == 'white'):
            result = engine.play(chess_board, chess.engine.Limit(time=0.1)).move
            print(result)
            chess_board.push(result)
            moves += 1
            chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as=PLAYER_COLOR)
            render_board(chess_board=chess_board, game_number="chess960")
        
    except Exception as e:
        print(e)
        engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")


    render_board(chess_board=chess_board, game_number="chess960")


render_board(chess_board=chess_board, game_number="chess960")

time.sleep(60)

engine.quit()
driver.quit()