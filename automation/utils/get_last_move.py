from selenium.webdriver.common.by import By
from player import FIGURINE

def get_last_move(driver: any ,turn: str) -> str:
    el = driver.find_element(By.CLASS_NAME, 'selected')
    if turn in el.get_attribute('class'):
        if FIGURINE:
            fig= ""
            try:
                fig += el.find_element(By.CSS_SELECTOR, 'span[data-figurine]').get_attribute('data-figurine')
            except:                                                                                         
                pass
            mv = fig + el.text if "=" not in el.text else el.text + fig
            if "#" in mv: mv = mv.replace("#", "")
            if "+" in mv and "=" in mv:
                mv = mv.replace("+", "") + "+"
            print("player:")
            print(mv)
            return mv
        else:
            return el.text