# source: https://github.com/DevMaxC/FastAPI-Selenium/blob/master/extract.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def run_headless_selenium(url: str ="https://www.chess.com/game/live/73925969651?username=hikaru"):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    
    # prefs = {"profile.managed_default_content_settings.images":2}
    # chrome_options.headless = True


    # chrome_options.add_experimental_option("prefs", prefs)
    # options=chrome_options
    # service=Service(ChromeDriverManager().install())
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-browser-side-navigation')
    chrome_options.add_argument('--disable-features=VizDisplayCompositor')
    chrome_options.add_argument('--mute-audio')

    capabilities = {
        "browserName": "chrome",
        "version": "latest",
        "platform": "ANY"
    }

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=chrome_options,
        desired_capabilities=capabilities
    )

    driver.get("https://www.google.com")
    print(driver.title)

    driver.quit()

    # myDriver = webdriver.Chrome()

    # return myDriver

# def createDriver():
#     firefox_options = webdriver.FirefoxOptions()
#     firefox_options.add_argument("--headless")
#     firefox_options.add_argument("--no-sandbox")
#     firefox_options.add_argument("--disable-dev-shm-usage")
#     firefox_options.add_argument("--window-size=1920,1080")
    
#     # prefs = {"profile.managed_default_content_settings.images":2}
#     firefox_options.headless = True
#     # chrome_options.add_experimental_option("prefs", prefs)

#     # source: https://pypi.org/project/webdriver-manager/
#     driver =  webdriver.Firefox(options=firefox_options)
#     return driver