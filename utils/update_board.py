
import chess
from selenium.webdriver.common.by import By

def update_board(driver: any, chess_board: chess.Board) -> None:
    print("started updating board")
    count = int(driver.find_element(By.CLASS_NAME, "selected").get_attribute("data-ply"))

    print(count)
    for i in range(count+1):
        try:
            chess_board.pop()
        except:
            pass

    print(chess_board)

    for i in range(1,count+1):
        fig= ""
        try:
            fig += driver.find_element(By.CSS_SELECTOR, f'[data-ply="{i}"]').find_element(By.CSS_SELECTOR, 'span[data-figurine]').get_attribute('data-figurine')
        except Exception as exception: pass
        mv = fig + driver.find_element(
            By.CSS_SELECTOR, f'[data-ply="{i}"]'
        ).text if "=" not in driver.find_element(
            By.CSS_SELECTOR, f'[data-ply="{i}"]'
        ).text else driver.find_element(By.CSS_SELECTOR, f'[data-ply="{i}"]').text + fig
        
        chess_board.push_san( mv )

    print(chess_board)
