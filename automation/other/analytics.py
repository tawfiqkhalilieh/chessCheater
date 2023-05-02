import chess
import chess.engine
import chess.svg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from constants import board as board
from selenium.webdriver.chrome.options import Options
import time
from automation.utils.render_board import render_board
from player import HEADLESS,FLIPPED_BOARD
from automation.utils.move import move as chess_move

board = board.white_board if not FLIPPED_BOARD else board.black_board
chess_board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")

# create a webdriver instance
options = Options()
if HEADLESS:
   options.add_argument("--headless")
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# navigate to a webpage
driver.get("https://www.chess.com/analysis")
actions = ActionChains(driver)

moves: int = 0
times = []

time.sleep(2)

while not chess_board.is_game_over():
    result = engine.play(chess_board, chess.engine.Limit(time=0.01)).move
    start_time = time.time()
    print(result)
    chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as='white' if not FLIPPED_BOARD else 'black')
    chess_board.push(result)
    times.append(time.time() - start_time)
    moves += 1
    render_board(chess_board=chess_board, game_number='analytics')
    

print(moves)
print(sum(times)/len(times))
driver.save_screenshot("automation/games/batata.png")

engine.quit()
driver.close()