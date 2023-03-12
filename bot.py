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
driver.get("https://www.chess.com/play/computer")
actions = ActionChains(driver)

driver.find_element(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']").click()

# board = {}
moves: int = 0

last_white= ""
last_black= ""

time.sleep(10)

def move(frm: str, to: str):
    driver.find_element(By.CLASS_NAME, board[frm]["square"]).click()
    actions.move_to_element(driver.find_element(By.CLASS_NAME, board[frm]["square"])).perform()
    action_chains2 = ActionChains(driver)
    action_chains2.move_by_offset(board[frm][to][0], board[frm][to][1]).click().perform()

try:
    while not chess_board.is_game_over():
        result = engine.play(chess_board, chess.engine.Limit(time=0.1))
        print(result.move)
        chess_board.push(result.move)
        move(str(result.move)[0] + str(result.move)[1], str(result.move)[2] + str(result.move)[3])
        last_white = result.move
        try:
            for el in driver.find_elements(By.CLASS_NAME, "promotion-piece"):
                if 'wq' in el.get_attribute('class'):
                    el.click()
        except:
            pass
        moves += 1
        time.sleep(4)
        mv = driver.find_element(By.CLASS_NAME, 'selected').text
        if "#" in mv:
            mv = mv.replace("#", "")
        
        chess_board.push_san(mv)
        

        with open("chess5.svg", 'w') as file:
            if chess.svg.board:
                file.write(chess.svg.board(
                    chess_board,
                    size=1000,
                ))
except Exception as e:
    print(e)
    with open("chess5.svg", 'w') as file:
            if chess.svg.board:
                file.write(chess.svg.board(
                    chess_board,
                    size=1000,
                ))

print(moves)

time.sleep(3600)

engine.quit()
# driver.close()