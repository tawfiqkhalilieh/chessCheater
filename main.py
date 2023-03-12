import chess
import chess.engine
import chess.svg

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random
from constants import board

chess_board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")
engine.configure(
    {
        "UCI_LimitStrength": True, 
        "UCI_Elo": 2100
    }
)

# create a webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# navigate to a webpage
driver.get("https://www.chess.com/play/computer")
driver.find_element(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']").click()

driver.find_element(By.CLASS_NAME, "login-modal-trigger").click()
time.sleep(0.5)
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("dasd12d23123")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("dsauiyshgSH0Asu012joi1e123123")
driver.find_element(By.ID, "login").click()

actions = ActionChains(driver)

moves: int = 0
GAME_MODE: str = "blitz"

time_lists = {
    "blitz": [0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 0.9999999999999999, 1.0999999999999999, 1.4, 1.7, 2.0, 2.3, 2.5999999999999996, 2.8999999999999995, 3.1999999999999993, 3.499999999999999, 3.799999999999999, 4.099999999999999, 4.399999999999999, 4.699999999999998, 4.999999999999998, 5.299999999999998, 5.599999999999998, 5.899999999999998, 6.1999999999999975, 6.499999999999997, 6.799999999999997, 7.099999999999997, 7.399999999999997, 7.699999999999997, 7.9999999999999964],
    "bullet": [0.1122121, 0.11111111, 0.145, 0.16, 0.22, 0.23, 0.32, 0.54, 0.76, 0.98, 1.2, 1.42],
    "rapid": [0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 0.9999999999999999, 1.0999999999999999, 1.4, 1.7, 2.0, 2.3, 2.5999999999999996, 2.8999999999999995, 3.1999999999999993, 3.499999999999999, 3.799999999999999, 4.099999999999999, 4.399999999999999, 4.699999999999998, 4.999999999999998, 5.299999999999998, 5.599999999999998, 5.899999999999998, 6.1999999999999975, 6.499999999999997, 6.799999999999997, 7.099999999999997, 7.399999999999997, 7.699999999999997, 7.9999999999999964, 8.299999999999997, 8.599999999999998, 8.899999999999999, 9.2, 9.5, 9.8, 10.100000000000001]
}

print("I'm ready")

def move(frm: str, to: str):
    driver.find_element(By.CLASS_NAME, board[frm]["square"]).click()
    actions.move_to_element(driver.find_element(By.CLASS_NAME, board[frm]["square"])).perform()
    action_chains2 = ActionChains(driver)
    action_chains2.move_by_offset(board[frm][to][0], board[frm][to][1]).click().perform()

def get_last_move():
    fig= ""
    try:
        fig += driver.find_element(By.CLASS_NAME, 'selected').find_element(By.CSS_SELECTOR, 'span[data-figurine]').get_attribute('data-figurine')
    except Exception as exception: pass
    print(fig + driver.find_element(By.CLASS_NAME, 'selected').text)
    return fig + driver.find_element(By.CLASS_NAME, 'selected').text if "=" not in driver.find_element(By.CLASS_NAME, 'selected').text else driver.find_element(By.CLASS_NAME, 'selected').text + fig

time_delay = lambda: 0.2 if "clock-low-time" in driver.find_element(By.CLASS_NAME, "clock-top").get_attribute('class') else random.choice(time_lists[GAME_MODE])

def game():
    with open("chess5.svg", 'w') as file:
        if chess.svg.board:
            file.write(chess.svg.board(
                chess_board,
                size=1000,
            ))

    chess_board.push_san( 
        get_last_move()
    )

    print("engine:")

    result = engine.play(chess_board, chess.engine.Limit(time=0.1))
    print(result.move)

    chess_board.push(result.move)

    move(str(result.move)[0] + str(result.move)[1], str(result.move)[2] + str(result.move)[3])
    try:
        for el in driver.find_elements(By.CLASS_NAME, "promotion-piece"):
            if 'wq' in el.get_attribute('class'):
                el.click()
    except:
        pass

    with open("chess5.svg", 'w') as file:
        if chess.svg.board:
            file.write(chess.svg.board(
                chess_board,
                size=1000,
            ))

r = input()

if not r:
    result = engine.play(chess_board, chess.engine.Limit(time=0.1))
    print(result.move)
    chess_board.push(result.move)
    move(str(result.move)[0] + str(result.move)[1], str(result.move)[2] + str(result.move)[3])
    moves += 1
else:
    game()
    moves+=1

try:
    while not chess_board.is_game_over():
        try:
            if ("clock-player-turn" not in driver.find_element(By.CLASS_NAME, "clock-top").get_attribute('class') and not r) or ("clock-player-turn" in driver.find_element(By.CLASS_NAME, "clock-top").get_attribute('class') and r):
                time.sleep(time_delay())
                game()
                moves+=1
        except Exception as e:
            print(e)
except Exception as e:
    print(chess_board)
    print(e)
    chess_board.pop()
    with open("chess5.svg", 'w') as file:
            if chess.svg.board:
                file.write(chess.svg.board(
                    chess_board,
                    size=1000,
                ))

print(moves)
engine.quit()
driver.close()