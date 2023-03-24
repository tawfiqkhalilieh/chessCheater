import chess
import chess.engine
import chess.svg
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from constants import board as board
from player import ELO, USERNAME, AUTO_PROMOTE_TO_QUEEN
from utils.login import login
from utils.move import move as chess_move
from utils.render_board import render_board
from utils.options import driver
from utils.update_board import update_board
from utils.get_last_move import get_last_move
from utils.next_game import next_game
from utils.is_ended import is_ended
from utils.time_delay import time_delay

chess_board: chess.Board = chess.Board()
engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")
engine.configure(
    {
        "UCI_LimitStrength": True, 
        "UCI_Elo": ELO
    }
)

# create a webdriver instance
actions: ActionChains = ActionChains(driver)

# navigate to the computer page
driver.get("https://www.chess.com/play/computer")
driver.find_element(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']").click()

login(driver=driver)

print("I'm ready")

def game():

    print("engine:")

    result = engine.play(chess_board, chess.engine.Limit(time=0.1))

    print(result.move)

    chess_board.push(result.move)
    
    try:
        chess_move(driver=driver,actions=actions, frm=str(result.move)[0] + str(result.move)[1], to=str(result.move)[2] + str(result.move)[3])
    except:
        print("Error while moving a piece")
        update_board(driver=driver, chess_board=chess_board)
        result = engine.play(chess_board, chess.engine.Limit(time=0.1))
        print(result.move)
        chess_board.push(result.move)

    # NOTE: should make it able to promote to all the possible pieces, it depends on the classname and the word in the move str
    if not AUTO_PROMOTE_TO_QUEEN and "=" in result.move:
        try:
            for el in driver.find_elements(By.CLASS_NAME, "promotion-piece"):
                if 'wq' in el.get_attribute('class'):
                    el.click()
        except:
            pass

    render_board(chess_board=chess_board)
    
input("Click Here to start")


while True:
    print("game started")

    print("Virtual Board Created")
    chess_board = chess.Board()

    print("fetching users")
    users_list= [ k.text for k in driver.find_elements(By.CSS_SELECTOR, '[data-test-element="user-tagline-username"]')]
    print(users_list)

    print("Writing the opponent name")
    with open('players.txt', "a") as fhandle:
        fhandle.write("\n")
        fhandle.write( users_list[0] if users_list[0] != USERNAME else users_list[1] )

    if users_list[-1] == USERNAME:
        # result = engine.play(chess_board, chess.engine.Limit(time=0.1))
        # print(result.move)
        # move(str(result.move)[0] + str(result.move)[1], str(result.move)[2] + str(result.move)[3])
        # chess_board.push(result.move)
        print("e2e4")
        chess_move(driver=driver, actions=actions, frm="e2", to="e4")
        chess_board.push_san("e2e4")

    print("waiting for the game to start")
    while not driver.find_elements(By.CLASS_NAME, "selected"):
        if is_ended(driver):
            break
    
    print("first move played")
    while not is_ended(driver):
        try:
            top_clock_turn = "clock-player-turn" not in driver.find_element(By.CLASS_NAME, "clock-top").get_attribute('class')
            if ( not top_clock_turn and users_list[-1] == USERNAME) or (top_clock_turn and users_list[-1] != USERNAME):
                last_move = get_last_move(driver, "black" if users_list[-1] == USERNAME else "white")
                while not last_move:
                    last_move = get_last_move(driver, "black" if users_list[-1] == USERNAME else "white")
                    if is_ended(driver):
                        break
                chess_board.push_san(
                    last_move
                )
                time.sleep(time_delay(driver, "white" if users_list[-1] == USERNAME else "black" ))
                game()
        except Exception as e:
            print(e)

    print("Game ended")
    next_game(driver,driver.current_url)
