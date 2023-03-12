# play quick game in the analytics

import chess
import chess.engine
import chess.svg

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from constants import board as board
import time

chess_board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")

# create a webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# navigate to a webpage
driver.get("https://www.chess.com/analysis")
actions = ActionChains(driver)


moves: int = 0

time.sleep(2)

def move(frm: str, to: str):
    driver.find_element(By.CLASS_NAME, board[frm]["square"]).click()
    actions.move_to_element(driver.find_element(By.CLASS_NAME, board[frm]["square"])).perform()
    action_chains2 = ActionChains(driver)
    action_chains2.move_by_offset(board[frm][to][0], board[frm][to][1]).click().perform()

try:
    while not chess_board.is_game_over():
        # time.sleep(0.1)
        result = engine.play(chess_board, chess.engine.Limit(time=0.1))
        print(result.move)
        chess_board.push(result.move)
        move(str(result.move)[0] + str(result.move)[1], str(result.move)[2] + str(result.move)[3])
        moves += 1
        try:
            for el in driver.find_elements(By.CLASS_NAME, "promotion-piece"):
                el.click()
        except:
            pass
except:
    print(moves)


print(moves)

time.sleep(3600)

engine.quit()
# driver.close()