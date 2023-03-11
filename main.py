import chess
import chess.engine
import chess.svg

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random

chess_board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")
# engine.configure({"UCI_LimitStrength": True, "UCI_Elo": 1500})


# create a webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# navigate to a webpage
driver.get("https://www.chess.com/play/computer")
driver.find_element(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']").click()

driver.find_element(By.CLASS_NAME, "login-modal-trigger").click()
time.sleep(0.5)
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("natayaho")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("natayahonatayahonatayahonatayahonatayahonatayahoA12")
driver.find_element(By.ID, "login").click()

actions = ActionChains(driver)

player_move2 = ""
board = {}
moves: int = 0
times_list = [0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 0.9999999999999999, 1.0999999999999999, 1.4, 1.7, 2.0, 2.3, 2.5999999999999996, 2.8999999999999995, 3.1999999999999993, 3.499999999999999, 3.799999999999999, 4.099999999999999, 4.399999999999999, 4.699999999999998, 4.999999999999998, 5.299999999999998, 5.599999999999998, 5.899999999999998, 6.1999999999999975, 6.499999999999997, 6.799999999999997, 7.099999999999997, 7.399999999999997, 7.699999999999997, 7.9999999999999964, 8.299999999999997, 8.599999999999998, 8.899999999999999, 9.2, 9.5, 9.8, 10.100000000000001]
print("I'm ready")

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

places = {
    "a1": chess.A1,
    "a2": chess.A2,
    "a3": chess.A3,
    "a4": chess.A4,
    "a5": chess.A5,
    "a6": chess.A6,
    "a7": chess.A7,
    "a8": chess.A8,
    "b1": chess.B1,
    "b2": chess.B2,
    "b3": chess.B3,
    "b4": chess.B4,
    "b5": chess.B5,
    "b6": chess.B6,
    "b7": chess.B7,
    "b8": chess.B8,
    "c1": chess.C1,
    "c2": chess.C2,
    "c3": chess.C3,
    "c4": chess.C4,
    "c5": chess.C5,
    "c6": chess.C6,
    "c7": chess.C7,
    "c8": chess.C8,
    "d1": chess.D1,
    "d2": chess.D2,
    "d3": chess.D3,
    "d4": chess.D4,
    "d5": chess.D5,
    "d6": chess.D6,
    "d7": chess.D7,
    "d8": chess.D8,
    "e1": chess.E1,
    "e2": chess.E2,
    "e3": chess.E3,
    "e4": chess.E4,
    "e5": chess.E5,
    "e6": chess.E6,
    "e7": chess.E7,
    "e8": chess.E8,
    "f1": chess.F1,
    "f2": chess.F2,
    "f3": chess.F3,
    "f4": chess.F4,
    "f5": chess.F5,
    "f6": chess.F6,
    "f7": chess.F7,
    "f8": chess.F8,
    "g1": chess.G1,
    "g2": chess.G2,
    "g3": chess.G3,
    "g4": chess.G4,
    "g5": chess.G5,
    "g6": chess.G6,
    "g7": chess.G7,
    "g8": chess.G8,
    "h1": chess.H1,
    "h2": chess.H2,
    "h3": chess.H3,
    "h4": chess.H4,
    "h5": chess.H5,
    "h6": chess.H6,
    "h7": chess.H7,
    "h8": chess.H8
}
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

turn = [False]
lastmoves = []


def move(frm: str, to: str):
    driver.find_element(By.CLASS_NAME, board[frm]["square"]).click()
    actions.move_to_element(driver.find_element(By.CLASS_NAME, board[frm]["square"])).perform()
    action_chains2 = ActionChains(driver)
    action_chains2.move_by_offset(board[frm][to][0], board[frm][to][1]).click().perform()


r = input()

if not r:
    result = engine.play(chess_board, chess.engine.Limit(time=0.1))
    print(result.move)
    chess_board.push(result.move)
    move(str(result.move)[0] + str(result.move)[1], str(result.move)[2] + str(result.move)[3])
    moves += 1

try:
    while not chess_board.is_game_over():
        try:
            if ("clock-player-turn" not in driver.find_element(By.CLASS_NAME, "clock-top").get_attribute('class') and not r) or ("clock-player-turn" in driver.find_element(By.CLASS_NAME, "clock-top").get_attribute('class') and r):
                
                    with open("chess5.svg", 'w') as file:
                        if chess.svg.board:
                            file.write(chess.svg.board(
                                chess_board,
                                size=1000,
                            ))

                    fig= ""  
                    player_move = driver.find_element(By.CLASS_NAME, 'selected').text

                    try:
                        fig += driver.find_element(By.CLASS_NAME, 'selected').find_element(By.CSS_SELECTOR, 'span[data-figurine]').get_attribute('data-figurine')
                    except Exception as exception: pass
                    
                    # time.sleep( 0.1 if moves < 5 else random.choice(times_list))
                    time.sleep(0.5)

                    mv = driver.find_element(By.CLASS_NAME, 'selected').text
                    if "#" in mv:
                        mv = mv.replace("#", "")
                    chess_board.push_san(fig + mv)


                    print("engine:")

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

                    with open("chess5.svg", 'w') as file:
                        if chess.svg.board:
                            file.write(chess.svg.board(
                                chess_board,
                                size=1000,
                            ))
            # else: print("waiting for my turn")
        except Exception as e:
            pass
            
        

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
