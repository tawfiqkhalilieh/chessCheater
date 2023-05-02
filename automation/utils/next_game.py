import time
from selenium.webdriver.common.by import By
from automation.utils.first_game import join_first_game
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def next_game(driver, prev_url):
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 20).until( EC.presence_of_element_located((By.CLASS_NAME, 'plus'))).click()
    except:
        print("please click on the next button")
    plys= driver.find_elements(By.CLASS_NAME, "selected")
    if len(plys) > 1:
        next_game(driver, driver.current_url)
    
    if "membership" in driver.current_url:
        driver.switch_to.window(list(driver.window_handles)[0])
        join_first_game(driver=driver)
    else:
        while prev_url == str(driver.current_url):
            time.sleep(1)
            if driver.find_elements(By.CLASS_NAME, 'alerts-message'):
                join_first_game(driver=driver)