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
from player import ELO, ACCOUNTS, HEADLESS
import sys
from automation.utils.options import driver
from selenium.webdriver.common.by import By
from automation.utils.login import login
from automation.utils.time_delay import time_delay
from automation.utils.is_ended import is_ended
from automation.utils.next_game import next_game

# pickup the user we want to use from the file call
# python main.py {account number}
if sys.argv:
    USERNAME = ACCOUNTS[int(sys.argv[1])-1][0]
else:
    USERNAME = ACCOUNTS[0][0]

chess_board: chess.Board = chess.Board(fen='8/8/8/8/8/8/8/8 w - - 0 1', chess960=True)

# setup and configure the engine
engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")
if ELO:
    engine.configure(
        {
            "UCI_LimitStrength": True, 
            "UCI_Elo": ELO
        }
    )

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

input("Click when you want me to start fetching")

loop = asyncio.get_event_loop()
chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))

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
            print(result.move)
            return str(result.move)
        except:
            chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))
            return get_best_move()
    
    
    # move the piece on chess.com
    
    def move_on_board(result):
        try:
            chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as= "white" if play_as_white else "black")
        except Exception as e:
            print(result)
            print(e)
            chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))
            if not is_ended(driver=driver):
                move_on_board(get_best_move())

    move_on_board(get_best_move())

    # draw the board in svg file ( for debugging uses )
    render_board(chess_board=chess_board, game_number=str(int(sys.argv[1])))

while True:
    print("game started")

    print("Virtual Board Created")

    chess_board= chess.Board(fen='8/8/8/8/8/8/8/8 w - - 0 1', chess960=True)
    chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))

    print("fetching users")

    play_as_white: bool = 'flipped' not in driver.find_element(By.ID, 'board-single').get_attribute('class')

    print("Writing the opponent name")
    # write the usernames in a text file to share them with chess.com
    with open('automation/players.txt', "a") as fhandle:
        fhandle.write("\n"+ [ k.text for k in driver.find_elements(By.CSS_SELECTOR, '[data-test-element="user-tagline-username"]')][0] )

    print("waiting for the game to start")

    if play_as_white:
        result = engine.play(chess_board, chess.engine.Limit(time=0.1)).move
        print(result)
        chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as= 'white' if play_as_white else 'black')
        chess_board.push(result)
    else:
        while not driver.find_elements(By.CLASS_NAME, "selected"):
            time.sleep(1)
            print("still waiting")
            if is_ended(driver):
                break
    
    while not is_ended(driver=driver):
        try:
            last_move = get_last_move(driver, 'black' if play_as_white else 'white')
            # fetch the last move and push it to the virtual chess board
            while not last_move:
                last_move = get_last_move(driver, 'black' if play_as_white else 'white')
                if is_ended(driver):
                    break
            try:
                chess_board.push_san(last_move)
            except:
                chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))

            # result = engine.play(chess_board, chess.engine.Limit(
            #     time=time_delay(driver=driver, turn= 'white' if play_as_white else 'black')
            #                                                      )).move
            # print(result)
            # chess_board.push(result)
            # chess_move(driver=driver,actions=actions, frm=str(result)[0] + str(result)[1], to=str(result)[2] + str(result)[3], play_as= 'white' if play_as_white else 'black')
            game(play_as_white=play_as_white)
        except:
            if is_ended(driver=driver):
                break
            else:
                chess_board = loop.run_until_complete(fetch_game(driver=driver, board=chess_board))
                engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")
    next_game(driver=driver, prev_url=driver.current_url)
