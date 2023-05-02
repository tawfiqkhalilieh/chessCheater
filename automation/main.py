import chess
import chess.engine
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from constants import board as board
from player import ELO, ACCOUNTS, HEADLESS, TOURNUMANTES
from automation.utils.login import login
from automation.utils.move import move as chess_move
from automation.utils.render_board import render_board
from automation.utils.options import driver
from automation.utils.update_board import update_board
from automation.utils.get_last_move import get_last_move
from automation.utils.next_game import next_game
from automation.utils.is_ended import is_ended
from automation.utils.time_delay import time_delay
from automation.utils.first_game import join_first_game
import sys

# pickup the user we want to use from the file call
# python main.py {account number}
if sys.argv:
    USERNAME = ACCOUNTS[int(sys.argv[1])-1][0]
    PASSWORD =  ACCOUNTS[int(sys.argv[1])-1][1]
else:
    USERNAME = ACCOUNTS[0][0]
    PASSWORD =  ACCOUNTS[0][1]

chess_board: chess.Board | None = None
# setup and configure the engine
engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")
if ELO:
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

driver.switch_to.window(list(driver.window_handles)[0])

# wait until the user enable the VPN and click on 'Start' Button
if HEADLESS:
    while not driver.find_elements(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']"):
        pass
    driver.find_element(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']").click()
else:
    while driver.find_elements(By.CSS_SELECTOR, "[data-cy='modal-first-time-button']"):
        pass

# login ( using the chess.com account from player.py )
login(driver=driver)

# join the first game and wait until the game starts
join_first_game(driver=driver)

def game(play_as_white):

    def get_best_move():
        try:
            # find a move to play
            result = engine.play(
                chess_board, chess.engine.Limit(
                    time=time_delay(driver, "white" if play_as_white else "black" )
                )
            )
            chess_board.push(result.move)
            return str(result.move)
        except:
            update_board(driver=driver, chess_board=chess_board)
            return get_best_move()
    
    
    # move the piece on chess.com
    
    def move_on_board(result):
        try:
            chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as= "white" if play_as_white else "black")
        except Exception as e:
            print(result)
            print(e)
            if not is_ended(driver=driver) and update_board(driver=driver, chess_board=chess_board) > 2:
                move_on_board(get_best_move())

    move_on_board(get_best_move())

    # draw the board in svg file ( for debugging uses )
    render_board(chess_board=chess_board, game_number=str(int(sys.argv[1])))

while True:
    if TOURNUMANTES:
        input("Click Here To Start")
    try:
        print("game started")

        print("Virtual Board Created")
        chess_board = chess.Board()

        print("fetching users")
        
        play_as_white: bool = 'flipped' not in driver.find_element(By.ID, 'board-single').get_attribute('class')

        print("Writing the opponent name")
        # write the usernames in a text file to share them with chess.com
        with open('automation/players.txt', "a") as fhandle:
            fhandle.write("\n"+ [ k.text for k in driver.find_elements(By.CSS_SELECTOR, '[data-test-element="user-tagline-username"]')][0] )

        print("waiting for the game to start")

        if play_as_white:
            # result = engine.play(chess_board, chess.engine.Limit(time=0.1))
            # print(result.move)
            # move(str(result.move)[0] + str(result.move)[1], str(result.move)[2] + str(result.move)[3])
            # chess_board.push(result.move)
            chess_move(driver=driver, actions=actions, frm="e2", to="e4", play_as= 'white' if play_as_white else 'black' )
            chess_board.push_san("e2e4")

        while not driver.find_elements(By.CLASS_NAME, "selected"):
            time.sleep(1)
            print("still waiting")
            if is_ended(driver):
                break

        print("first move played")
        while not is_ended(driver):
            try:
                if driver.find_elements(By.CLASS_NAME, 'alerts-message'):
                    driver.get(driver.current_url)
                last_move = get_last_move(driver, 'black' if play_as_white else 'white')
                # fetch the last move and push it to the virtual chess board
                while not last_move:
                    last_move = get_last_move(driver, 'black' if play_as_white else 'white')
                    if is_ended(driver):
                        break

                chess_board.push_san(
                    last_move
                )

                # time delay between the moves
<<<<<<< HEAD
                # time.sleep(time_delay(driver, "white" if play_as_white else "black" ))
=======
                time.sleep(time_delay(driver, "white" if play_as_white else "black" ))
>>>>>>> 16a0c5201455aece0f662002bcaf816cb11e9fa6

                # play engine move
                game(play_as_white=play_as_white)
            except Exception as e:
                print(e)
                update_board(driver=driver, chess_board=chess_board)
        print("Game ended")
        if not TOURNUMANTES:
            next_game(driver,driver.current_url)
    except Exception as e:
        print(e)
        update_board(driver=driver, chess_board=chess_board)
        if is_ended(driver):
            next_game(driver,driver.current_url)
