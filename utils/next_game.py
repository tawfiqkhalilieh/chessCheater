import time
from selenium.webdriver.common.by import By

def next_game(driver, prev_url):
    time.sleep(0.5)
    try:
        driver.find_element(By.CSS_SELECTOR, '[data-cy="sidebar-game-over-new-game-button"]').click()
    except:
        print("please click on the next button")
    plys= driver.find_elements(By.CLASS_NAME, "selected")
    if len(plys) > 1:
        next_game(driver, driver.current_url)
    
    while prev_url == str(driver.current_url):
        pass

    if "membership" in driver.current_url:
        driver.get(prev_url)
        next_game(driver, prev_url)