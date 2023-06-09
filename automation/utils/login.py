from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from player import ACCOUNTS
import sys

if sys.argv:
    USERNAME = ACCOUNTS[int(sys.argv[1])-1][0]
    PASSWORD =  ACCOUNTS[int(sys.argv[1])-1][1]
else:
    USERNAME = ACCOUNTS[0][0]
    PASSWORD =  ACCOUNTS[0][1]

def login(driver):
    WebDriverWait(
        driver, 10
    ).until( 
        EC.presence_of_element_located((By.CLASS_NAME, "login-modal-trigger"))
    ).click()
    WebDriverWait(
        driver, 10
    ).until( 
        EC.presence_of_element_located((By.ID, "username"))
    ).click()
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login").click()