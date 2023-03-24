import platform
from selenium import webdriver

options = None
driver = None

if "Windows" in platform.platform():
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-infobars")
    driver = webdriver.Chrome(options=options)

# TODO: add Linux and MacOs options (firefox and safari)