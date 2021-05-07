#Python class who contain all function who need to be lunched for the bot working
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import conf.Constants as constants
from random import uniform

def setUpProxy(capabilities):
    index = int(uniform(0, len(constants.PROXIES)))
    PROXY = constants.PROXIES[index]["host"] + ":" + str(constants.PROXIES[index]["port"])
    capabilities['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY
    }

def setUpChromeDriver():
    driver = webdriver.Chrome(executable_path=constants.CHROME_DRIVER_PATH, chrome_options=getChromeOptions(),
                              desired_capabilities= getChromeCapabilities())
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    print(driver.execute_script("return navigator.userAgent;"))
    driver.set_window_size(929, 1012)
    return driver

def getChromeOptions():
    option = webdriver.ChromeOptions()
    option.add_argument('log-level=3')
    option.add_argument("start-maximized")
    option.binary_location = constants.BRAVE_PATH
    option.add_experimental_option("useAutomationExtension", "true")
    option.add_extension("./asset/extension/Buster.crx")
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('useAutomationExtension', False)
    prefs = {"profile.password_manager_enabled": False, "credentials_enable_service": False}
    option.add_argument('--disable-gpu')
    option.add_argument('--no-sandbox')
    option.add_experimental_option("prefs", prefs)
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    #option.add_argument(f'user-agent={user_agent}')

def getChromeCapabilities():
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}
    #setUpProxy(capabilities, constants.PROXY)
    return capabilities