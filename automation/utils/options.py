from selenium import webdriver
from player import HEADLESS
from selenium_stealth import stealth

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")
if HEADLESS:
    options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_extension('./automation/utils/extensions/vpn.crx')
driver = webdriver.Chrome(options=options)

stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

driver.maximize_window()
