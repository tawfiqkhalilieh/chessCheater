from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from player import AUTO_PROMOTE_TO_QUEEN
from constants import board

def move(driver: any,actions: ActionChains, frm: str, to: str, play_as: str) -> None:

    data_board = board.white_board if play_as == "white" else board.black_board

    try:
        actions.move_to_element(
            driver.find_element(By.CLASS_NAME, data_board[frm]["square"])
        )\
                .click()\
                .move_by_offset(data_board[frm][to][0], data_board[frm][to][1])\
                .click()\
                .perform()
    except Exception as e:
        print(e)
    
    try:
        driver.find_elements(By.CLASS_NAME, "promotion-piece")[-1].click()
    except:
        pass
