# play quick game in the analytics

import chess
import chess.engine
import chess.svg

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

chess_board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")

# create a webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# navigate to a webpage
driver.get("https://www.chess.com/analysis")
actions = ActionChains(driver)


board = {}
moves: int = 0

# Loop through each square on the board
for file in "abcdefgh":
    for rank in range(1, 9):
        square = file + str(rank)
        board[square] = {"square": f"square-{(rank-1)*8 + (ord(file)-ord('a'))}"}
        
        # Loop through every other square on the board
        for other_file in "abcdefgh":
            for other_rank in range(1, 9):
                other_square = other_file + str(other_rank)
                
                # Calculate the x and y distances between the two squares
                x_distance = (ord(other_file) - ord(file)) * 100
                y_distance = ((other_rank - rank) * 100) * -1
                
                # Add the distance to the dictionary
                board[square][other_square] = (x_distance, y_distance)

board["a1"]["square"] = "square-11"
board["a2"]["square"] = "square-12"
board["a3"]["square"] = "square-13"
board["a4"]["square"] = "square-14"
board["a5"]["square"] = "square-15"
board["a6"]["square"] = "square-16"
board["a7"]["square"] = "square-17"
board["a8"]["square"] = "square-18"

board["b1"]["square"] = "square-21"
board["b2"]["square"] = "square-22"
board["b3"]["square"] = "square-23"
board["b4"]["square"] = "square-24"
board["b5"]["square"] = "square-25"
board["b6"]["square"] = "square-26"
board["b7"]["square"] = "square-27"
board["b8"]["square"] = "square-28"

board["c1"]["square"] = "square-31"
board["c2"]["square"] = "square-32"
board["c3"]["square"] = "square-33"
board["c4"]["square"] = "square-34"
board["c5"]["square"] = "square-35"
board["c6"]["square"] = "square-36"
board["c7"]["square"] = "square-37"
board["c8"]["square"] = "square-38"

board["d1"]["square"] = "square-41"
board["d2"]["square"] = "square-42"
board["d3"]["square"] = "square-43"
board["d4"]["square"] = "square-44"
board["d5"]["square"] = "square-45"
board["d6"]["square"] = "square-46"
board["d7"]["square"] = "square-47"
board["d8"]["square"] = "square-48"

board["e1"]["square"] = "square-51"
board["e2"]["square"] = "square-52"
board["e3"]["square"] = "square-53"
board["e4"]["square"] = "square-54"
board["e5"]["square"] = "square-55"
board["e6"]["square"] = "square-56"
board["e7"]["square"] = "square-57"
board["e8"]["square"] = "square-58"

board["f1"]["square"] = "square-61"
board["f2"]["square"] = "square-62"
board["f3"]["square"] = "square-63"
board["f4"]["square"] = "square-64"
board["f5"]["square"] = "square-65"
board["f6"]["square"] = "square-66"
board["f7"]["square"] = "square-67"
board["f8"]["square"] = "square-68"

board["g1"]["square"] = "square-71"
board["g2"]["square"] = "square-72"
board["g3"]["square"] = "square-73"
board["g4"]["square"] = "square-74"
board["g5"]["square"] = "square-75"
board["g6"]["square"] = "square-76"
board["g7"]["square"] = "square-77"
board["g8"]["square"] = "square-78"

board["h1"]["square"] = "square-81"
board["h2"]["square"] = "square-82"
board["h3"]["square"] = "square-83"
board["h4"]["square"] = "square-84"
board["h5"]["square"] = "square-85"
board["h6"]["square"] = "square-86"
board["h7"]["square"] = "square-87"
board["h8"]["square"] = "square-88"

time.sleep(2)

def move(frm: str, to: str):
    driver.find_element(By.CLASS_NAME, board[frm]["square"]).click()
    actions.move_to_element(driver.find_element(By.CLASS_NAME, board[frm]["square"])).perform()
    action_chains2 = ActionChains(driver)
    action_chains2.move_by_offset(board[frm][to][0], board[frm][to][1]).click().perform()

try:
    while not chess_board.is_game_over():
        # time.sleep(0.1)
        result = engine.play(chess_board, chess.engine.Limit(time=1))
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