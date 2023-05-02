import chess
import chess.engine
import chess.svg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from constants import board as board
import time
from player import HEADLESS
from selenium.webdriver.chrome.options import Options
from automation.utils.render_board import render_board
import asyncio
from automation.utils.get_last_move import get_last_move
from automation.utils.move import move as chess_move
from player import PLAYER_COLOR

chess_board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")

# create a webdriver instance
options = Options()
if HEADLESS:
   options.add_argument("--headless")
#    options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# navigate to a webpage
driver.get("https://www.chess.com/play/computer")
actions = ActionChains(driver)
driver.find_element(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']").click()

moves: int = 0

time.sleep(2)

loop = asyncio.get_event_loop()

if PLAYER_COLOR == "black":
    chess_board.push_san(get_last_move(driver=driver,turn= "white" if PLAYER_COLOR == "black" else "black"))


while not chess_board.is_game_over():
    try:
        if ( chess_board.turn == chess.BLACK and PLAYER_COLOR == 'black') or ( chess_board.turn == chess.WHITE and PLAYER_COLOR == 'white'):
            result = engine.play(chess_board, chess.engine.Limit(time=0.1)).move
            print(result)
            chess_board.push(result)
            moves += 1
            loop.run_until_complete(chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as=PLAYER_COLOR))
            render_board(chess_board=chess_board, game_number=88)
        time.sleep(4)

        chess_board.push_san(get_last_move(driver=driver,turn= "white" if PLAYER_COLOR == "black" else "black"))
        
    except:
        pass
    render_board(chess_board=chess_board, game_number='bot')
<<<<<<< HEAD
    driver.save_screenshot("games/bot.png")
=======
    driver.save_screenshot("automation/games/bot.png")
>>>>>>> 16a0c5201455aece0f662002bcaf816cb11e9fa6

print(moves)
time.sleep(180)

engine.quit()
driver.close()