from selenium.webdriver.common.by import By
import time
from player import HEADLESS

def join_first_game(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'modal-trial-footer').click()
    except:
        pass

    driver.get("https://www.chess.com/play/online/new")

    if HEADLESS:
        while not driver.find_elements(By.CSS_SELECTOR, '[data-cy="new-game-index-play"]'):
            driver.save_screenshot("automation/games/onlinebatata.png")
            time.sleep(1)

    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[data-cy="new-game-index-play"]').click()

    if HEADLESS:
        while not driver.find_elements(By.CLASS_NAME, 'nav-link-text'):
            driver.save_screenshot("automation/games/onlinebatata.png")
            time.sleep(1)
    
    while "live" not in driver.current_url:
        pass