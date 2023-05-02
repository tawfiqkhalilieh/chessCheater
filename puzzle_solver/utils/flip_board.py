from selenium.webdriver.common.by import By

def flip_board(driver, actions):
    filp_element = driver.find_element(By.ID, 'board-layout-controls')
    actions.move_to_element(
        filp_element
    ).perform()
    driver.find_element(By.CSS_SELECTOR, '[aria-label="Flip Board"]').click()