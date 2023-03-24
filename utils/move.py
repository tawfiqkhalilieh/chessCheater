from constants import board
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def move(driver: any,actions: ActionChains, frm: str, to: str) -> None:
    actions.move_to_element(
        driver.find_element(By.CLASS_NAME, board[frm]["square"])
    )\
            .click()\
            .move_by_offset(board[frm][to][0], board[frm][to][1])\
            .click()\
            .perform()