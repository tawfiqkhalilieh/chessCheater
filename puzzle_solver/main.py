import chess
import chess.engine
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from puzzle_solver.utils.fetch_game import fetch_game
import time
import asyncio
from automation.utils.move import move as chess_move
from player import THINKING_TIME

engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument('--start-maximized')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
actions: ActionChains = ActionChains(driver)

driver.get("https://www.chess.com/analysis?tab=analysis")

board: chess.Board = chess.Board()
board.clear()

def who_to_play():
    try:
        return chess.WHITE if "white" in driver.find_element(By.CLASS_NAME, 'message-color-to-move-component').text.lower() else chess.BLACK
    except:
        pass
    try:
        return chess.WHITE if "white" in driver.find_element(By.CLASS_NAME, 'section-heading-title').text.lower() else chess.BLACK
    except:
        pass

    return who_to_play()

def who_to_play_str():
    try:
        return "white" if "white" in driver.find_element(By.CLASS_NAME, 'message-color-to-move-component').text.lower() else 'black'
    except:
        pass
    try:
        return "white" if "white" in driver.find_element(By.CLASS_NAME, 'section-heading-title').text.lower() else 'black'
    except:
        pass

    return who_to_play_str()

input()        

# source: https://www.geeksforgeeks.org/how-to-run-two-async-functions-forever-python/
loop = asyncio.get_event_loop()

while True:
    try:
        loop.run_until_complete(fetch_game(driver, board))

        board.turn = who_to_play()

        time.sleep(1)
        # here we run stockfish on depth: 30
        result = engine.play(board, chess.engine.Limit(time=THINKING_TIME))
        print(result.move)
        
        
        chess_move(
            driver=driver,
            actions=actions, 
            frm=str(result.move)[0] + str(result.move)[1], 
            to=str(result.move)[2] + str(result.move)[3],
            play_as=who_to_play_str()
        )
        
        try:
            driver.find_elements(By.CLASS_NAME, "promotion-piece")[-1].click()
        except:
            pass
    
    except Exception as e:
        print("err: " + str(e))
        engine: chess.engine.SimpleEngine = chess.engine.SimpleEngine.popen_uci(r"fish.exe")