from selenium.webdriver.common.by import By
from player import time_lists, GAME_MODE
import random

time_delay = lambda driver, turn: 0.1 if "clock-low-time" in driver.find_element(By.CLASS_NAME, "clock-top" if turn == "white" else "clock-bottom").get_attribute('class') else random.choice(time_lists[GAME_MODE])