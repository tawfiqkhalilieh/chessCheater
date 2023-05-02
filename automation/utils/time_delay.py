from selenium.webdriver.common.by import By
from player import time_lists, GAME_MODE, HACKERMODE
import random

time_delay = lambda driver, turn: 0.01 if "clock-low-time" in driver.find_element(By.CLASS_NAME, "clock-top" if turn == "white" else "clock-bottom").get_attribute('class') or HACKERMODE else random.choice(time_lists[GAME_MODE])