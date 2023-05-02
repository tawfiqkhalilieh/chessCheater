from app.services.utils.create_selenium_driver import run_headless_selenium
from selenium.webdriver.common.by import By
import re
from app.services.utils.format_time import format_time

def learn_game(game_url: str):
    driver = run_headless_selenium()
    # driver.quit()
    return "I'm happy"
    # driver.get(game_url)

    # data: dict = {}
    # i: int = 1

    # match = re.search(r'/(\d+)\?', game_url)

    # data["game_id"] = match.group(1) if match and "https://www.chess.com/game/live/" in game_url else "Game ID not found"
    # data["game_url"] = game_url

    # turns = driver.find_elements(
    #     By.CLASS_NAME, "move"
    # )

    # while not turns:
    #     turns = driver.find_elements(
    #         By.CLASS_NAME, "move"
    #     )

    # for turn in turns:
    #     el = turn.find_elements(
    #             By.CSS_SELECTOR, '[data-vml-element="timestamp"]'
    #         )
    #     data[i] = {}
        
    #     data[i]["white"] = float(format_time(el[0].text))
    #     if len(el) > 1:
    #         data[i]["black"] = float(format_time(el[1].text))
    #     i+=1
    # return data
