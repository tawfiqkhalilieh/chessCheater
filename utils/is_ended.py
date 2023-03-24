from selenium.webdriver.common.by import By

is_ended = lambda driver: bool(driver.find_elements(By.CLASS_NAME, "board-modal-header-component"))