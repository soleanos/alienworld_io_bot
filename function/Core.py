## Python class who contain principals function used by the alienabot

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import conf.Constants as constants
import function.Utils as utils
import conf.Personal as personal
import function.Init as init
import function.Captcha as captcha
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
from anticaptchaofficial.recaptchav2proxyless import *

## VARIABLES
driver = init.setUpChromeDriver()
debugBarsAdd = 1
size = 0,0
driver.switch_to.default_content()
driver.get(constants.WAX_WALLET_LOGIN_URL)

## CORE FUNCTIONS

def preload(): # logs into wax.io
    utils.log("Preloading...")
    utils.random_sleeping()
    ActionChains(driver).move_by_offset(513, 187).click().perform()
    ActionChains(driver).move_by_offset(-513, -187).click().perform()
    while True:
        utils.log("Logging in")
        try:
            driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input').send_keys(personal.REDDIT_USERNAME)
            driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[2]/input').send_keys(personal.REDDIT_PASSWORD)
            driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()
        except:
            time.sleep(0.1)
        else:
            break
    time.sleep(2)
    while True:
        utils.log("Allowing")
        try:
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div/input[1]').click()
        except:
            time.sleep(0.5)
        else:
            break
    time.sleep(3)
    while True:
        if driver.current_url != constants.WAX_WALLET_DASHBOARD_URL:
            utils.log("Waiting for dashboard")
            time.sleep(0.6)
        else:
            break
    utils.log("Switching to AW")
    driver.get(constants.ALIENWORD_URL)
    global size
    utils.log(f"DebugRes = {constants.DEBUG_RESOLUTION}")
    utils.log(f"Size = {size}")
    if constants.DEBUG_RESOLUTION == False:
        size = driver.get_window_size()["width"]/0.5625, driver.get_window_size()["height"]
    if constants.DEBUG_RESOLUTION == True:
        size = 500, 500
    utils.log(f"Size = {size}")
    print(size)
    utils.log(f"Set window to size")
    driver.set_window_size(size[0], size[1])


def login(): # login into alienworlds
    found = False
    time.sleep(5)
    while not found:
        utils.log(f"Waiting for login")
        for e in driver.get_log('browser'):
            if "Input Manager initialize...\\n" in e["message"]:
                found = True
                break
        time.sleep(0.5)
    global size
    while True:
        _debugLog = driver.get_log('browser')
        driver.set_window_size(size[0], size[1])
        x = driver.get_window_size()["width"]/2
        y = driver.get_window_size()["height"]*0.621761
        if constants.DEBUG_RESOLUTION == True:
            x, y = 250, 233
        utils.log(f"X, Y = {x}, {y}")
        utils.log(f"Clicking")
        ActionChains(driver).move_by_offset(x, y).click().perform()
        time.sleep(0.2)
        utils.log(f"Backing")
        ActionChains(driver).move_by_offset(-x, -y).click().perform()
        time.sleep(5)
        global debugBarsAdd
        if driver.get_log('browser') == _debugLog:
            if debugBarsAdd > 2:
                utils.log(f"Reverse scaling window to {size}, {debugBarsAdd}")
                size = size[0], size[1]-25
                debugBarsAdd = 0
            else:
                utils.log(f"Scaling window to {size}, {debugBarsAdd}")
                size = size[0], size[1]+25
                debugBarsAdd += 1
        else:
            break


def miner(force = False): # activates miner menu button
    print(driver.window_handles)
    found = False
    while not found:
        utils.log(f"Waiting for miner")
        if force == True:
            utils.log(f"Force miner")
            break
        for e in driver.get_log('browser'):
            if "successfully downloaded and stored in the indexedDB cache" in e["message"]:
                found = True
                break
        time.sleep(0.6)
    driver.set_window_size(size[0], size[1])
    x = driver.get_window_size()["width"]/1.32714285714
    y = driver.get_window_size()["height"]/3.4
    if constants.DEBUG_RESOLUTION == True:
        x, y = 405, 105
    utils.log(f"X, Y = {x}, {y}")
    utils.log(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()
    time.sleep(0.2)
    utils.log(f"Backing")
    ActionChains(driver).move_by_offset(-x, -y).click().perform()

def mine(force = False): # starts mining
    found = False
    while not found:
        utils.log(f"Waiting for mine")
        if force == True:
            utils.log(f"Force mine")
            break
        for e in driver.get_log('browser'):
            if "successfully downloaded and stored in the indexedDB cache" in e["message"]:
                found = True
                break
        time.sleep(0.6)
    driver.set_window_size(size[0], size[1])
    x = driver.get_window_size()["width"]/2
    y = driver.get_window_size()["height"]/1.35
    if constants.DEBUG_RESOLUTION == True:
        x, y = 250, 275
    utils.log(f"X, Y = {x}, {y}")
    utils.log(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()
    time.sleep(0.2)
    utils.log(f"Backing")
    ActionChains(driver).move_by_offset(-x, -y).click().perform()



def get(force = False): # claims reward
    found = False
    while not found:
        for e in driver.get_log('browser'):
            if "end doWork" in e["message"]:
                found = True
                break
        time.sleep(0.6)

    driver.set_window_size(size[0], size[1])
    x = driver.get_window_size()["width"]/2
    y = driver.get_window_size()["height"]/1.9
    if constants.DEBUG_RESOLUTION == True:
        x, y = 204, 194
    utils.log(f"X, Y = {x}, {y}")
    utils.log(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()
    ActionChains(driver).move_by_offset(-x, -y).click().perform()

    utils.random_sleeping()

    window_principal = driver.window_handles[0]
    window_popup = driver.window_handles[1]
    driver.switch_to.window(window_popup)
    utils.random_sleeping()
    driver.switch_to.default_content()

    captcha.solveCaptcha(driver)

    utils.log(f"Approving transaction")
    ActionChains(driver).move_by_offset(299,651 ).click().perform()
    ActionChains(driver).move_by_offset(-299,-651).click().perform()
    driver.switch_to.window(window_principal)
    driver.switch_to.default_content()


def end(force = False): # resets
    found = False
    while not found:
        utils.log(f"Waiting for end")
        if force == True:
            utils.log(f"Force end")
            break
        for e in driver.get_log('browser'):
            if "Loaded Mining" in e["message"]:
                found = True
                print(found)
                break
        time.sleep(0.6)
    time.sleep(10)
    driver.set_window_size(size[0], size[1])
    x = driver.get_window_size()["width"]/4.05
    y = driver.get_window_size()["height"]/1.52025316456
    if constants.DEBUG_RESOLUTION == True:
        x, y = 140, 250
    utils.log(f"X, Y = {x}, {y}")
    utils.log(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()
    time.sleep(0.2)
    utils.log(f"Backing")
    ActionChains(driver).move_by_offset(-x, -y).click().perform()

def wait(): # finds sleep time and waits
    s = ""
    found = False
    while not found:
        for e in driver.get_log('browser'):
            if "until next mine" in e["message"]:
                found = True
                s = e["message"]
                break
        time.sleep(0.6)
    utils.log("Sleeping")
    time.sleep(int(s[s.find("mine ")+5:s.find("\"'")])/1000)
    utils.log("SleepStop")

