import random
import time
import scipy.interpolate as si
from datetime import datetime
import os
from random import uniform, randint
import numpy as np
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#https://github.com/teal33t/captcha_bypass/blob/12cd04b3a66a11704bc6da610964ffe01fa06856/recaptcha_buster_bypass.py#L98

PROXY =[
{"host": "34.65.217.248", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.15, "error_rate": 0.0},
{"host": "198.46.160.38", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.36, "error_rate": 0.0},
{"host": "18.162.100.154", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.62, "error_rate": 0.0},
{"host": "18.210.69.172", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.22, "error_rate": 0.0},
{"host": "204.12.202.198", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.3, "error_rate": 0.0},
{"host": "23.237.100.74", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.32, "error_rate": 0.0},
{"host": "206.189.192.5", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.63, "error_rate": 0.0},
{"host": "23.237.173.109", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.4, "error_rate": 0.0},
{"host": "167.71.83.150", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.41, "error_rate": 0.0},
{"host": "34.93.171.222", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.92, "error_rate": 0.0},
{"host": "157.245.67.128", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.61, "error_rate": 0.0},
{"host": "18.162.89.135", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.71, "error_rate": 0.0},
{"host": "198.98.55.168", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.65, "error_rate": 0.0},
{"host": "157.245.124.217", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.7, "error_rate": 0.0},
{"host": "129.146.181.251", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.76, "error_rate": 0.0},
{"host": "134.209.188.111", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.78, "error_rate": 0.0},
{"host": "68.183.191.140", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.82, "error_rate": 0.0},
{"host": "35.192.138.9", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.29, "error_rate": 0.0},
{"host": "157.245.207.112", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.85, "error_rate": 0.0},
{"host": "68.183.191.248", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.87, "error_rate": 0.0},
{"host": "165.22.54.37", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.88, "error_rate": 0.0},
{"host": "71.187.28.75", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.34, "error_rate": 0.0},
{"host": "157.245.205.81", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.92, "error_rate": 0.0},
{"host": "45.76.255.157", "port": 808, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.45, "error_rate": 0.0},
{"host": "157.245.197.92", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.01, "error_rate": 0.0},
{"host": "159.203.87.130", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.47, "error_rate": 0.0},
{"host": "50.195.185.171", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.03, "error_rate": 0.0},
{"host": "144.202.20.56", "port": 808, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.51, "error_rate": 0.0},
{"host": "157.230.250.116", "port": 8080, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 1.14, "error_rate": 0.0},
{"host": "104.196.70.154", "port": 3128, "geo": {"country": {"code": "US", "name": "United States"}, "region": {"code": "Unknown", "name": "Unknown"}, "city": "Unknown"}, "types": [{"type": "HTTPS", "level": ""}], "avg_resp_time": 0.64, "error_rate": 0.0}
]

# Randomization Related
MIN_RAND = 0.64
MAX_RAND = 1.27
LONG_MIN_RAND = 4.78
LONG_MAX_RAND = 11.1

index = int(uniform(0, len(PROXY)))
PROXY = PROXY[index]["host"]+":"+str(PROXY[index]["port"])

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
driver_path = "C:/Driver/chromedriver.exe" # location of your chromedriver
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # location of your Brave browser

capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = { 'browser':'ALL' }

option = webdriver.ChromeOptions()
option.add_argument('log-level=3')
option.add_argument("start-maximized")

#option.add_argument('window-size=929, 1012')
option.binary_location = brave_path
option.add_experimental_option("useAutomationExtension","true")
option.add_extension(ROOT_DIR+"\Buster.crx")
ua = UserAgent()
userAgent = ua.random
print(userAgent)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

#option.add_argument('--user-agent={userAgent}')
#option.add_argument('--proxy-server=%s' % PROXY)

option.add_argument('--disable-blink-features=AutomationControlled')
option.add_experimental_option('useAutomationExtension', False)
#option.add_experimental_option("excludeSwitches", ["enable-automation"])
prefs = {"profile.password_manager_enabled": False, "credentials_enable_service": False}
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')
option.add_experimental_option("prefs", prefs)
option.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option, desired_capabilities=capabilities)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
print(driver.execute_script("return navigator.userAgent;"))
driver.set_window_size(929, 1012)


driver.switch_to.default_content()
main_page = driver.current_window_handle

###
reddit_username = "antho85180"
reddit_password = "Savary85!"
sleeptimeMin = 30 # Minimum time the bot will sleep between actions to look more human
sleeptimeMax = 90 # Maximum time the bot will sleep between actions to look more human
###
debugResolution = True
debugBarsAdd = 0
debugLogfile = "debug.log"
###
version = "1.1.4"
###

driver.get("https://wallet.wax.io/")


# Simple logging method
def log(s, t=None):
    now = datetime.now()
    if t == None:
        t = "Main"
    print("%s :: %s -> %s " % (str(now), t, s))

def debugger(t = "init"):
    nl = "\n"
    if t == "init":
        f = open(debugLogfile, "w+")
        f.write(f"AWA {version} | {datetime.now().strftime('%c')}{nl}")
        f.close()
    else:
        f = open(debugLogfile, "a")
        print(t)
        f.write(f"{datetime.now().strftime('%X')} | {t}{nl}")
        f.close()


def sleeptime():
    x = random.randint(sleeptimeMin, sleeptimeMax)
    print(f"Going sleep: {x}s")
    return x

size = 0,0

def preload(): # logs into wax.io
    debugger("Preloading...")
    while True:
        debugger("Clicking Reddit loggin")
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[4]/div/div[9]/button').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/div[3]/div[1]/div[9]/button').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[4]/div[1]/div[9]/button').click()
        except:
            if driver.current_url.startswith("https://www.reddit.com/"):
                debugger("Website is reddit, breaking")
                break
            else:
                time.sleep(0.5)
        else:
            break
    while True:
        debugger("Logging in")
        try:
            driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input').send_keys(reddit_username)
            driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[2]/input').send_keys(reddit_password)
            driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button').click()
        except:
            time.sleep(0.1)
        else:
            break
    time.sleep(2)
    while True:
        debugger("Allowing")
        try:
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div/input[1]').click()
        except:
            time.sleep(0.5)
        else:
            break
    time.sleep(3)
    while True:
        if driver.current_url != "https://wallet.wax.io/dashboard":
            debugger("Waiting for dashboard")
            time.sleep(0.6)
        else:
            break
    debugger("Switching to AW")
    driver.get("https://play.alienworlds.io/")
    global size
    debugger(f"DebugRes = {debugResolution}")
    debugger(f"Size = {size}")
    if debugResolution == False:
        size = driver.get_window_size()["width"]/0.5625, driver.get_window_size()["height"]
    if debugResolution == True:
        size = 500, 500
    debugger(f"Size = {size}")
    print(size)
    debugger(f"Set window to size")
    driver.set_window_size(size[0], size[1])


def login(): # login into alienworlds
    found = False
    time.sleep(5)
    while not found:
        debugger(f"Waiting for login")
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
        if debugResolution == True:
            x, y = 250, 233
        debugger(f"X, Y = {x}, {y}")
        debugger(f"Clicking")
        ActionChains(driver).move_by_offset(x, y).click().perform()
        time.sleep(0.2)
        debugger(f"Backing")
        ActionChains(driver).move_by_offset(-x, -y).click().perform()
        time.sleep(5)
        global debugBarsAdd
        if driver.get_log('browser') == _debugLog:
            if debugBarsAdd > 2:
                debugger(f"Reverse scaling window to {size}, {debugBarsAdd}")
                size = size[0], size[1]-25
                debugBarsAdd = 0
            else:
                debugger(f"Scaling window to {size}, {debugBarsAdd}")
                size = size[0], size[1]+25
                debugBarsAdd += 1
        else:
            break


def miner(force = False): # activates miner menu button
    print(driver.window_handles)
    found = False
    while not found:
        debugger(f"Waiting for miner")
        if force == True:
            debugger(f"Force miner")
            break
        for e in driver.get_log('browser'):
            if "successfully downloaded and stored in the indexedDB cache" in e["message"]:
                found = True
                break
        time.sleep(0.6)
    driver.set_window_size(size[0], size[1])
    x = driver.get_window_size()["width"]/1.32714285714
    y = driver.get_window_size()["height"]/3.4
    if debugResolution == True:
        x, y = 405, 105
    debugger(f"X, Y = {x}, {y}")
    debugger(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()
    time.sleep(0.2)
    debugger(f"Backing")
    ActionChains(driver).move_by_offset(-x, -y).click().perform()

def mine(force = False): # starts mining
    found = False
    while not found:
        debugger(f"Waiting for mine")
        if force == True:
            debugger(f"Force mine")
            break
        for e in driver.get_log('browser'):
            if "successfully downloaded and stored in the indexedDB cache" in e["message"]:
                found = True
                break
        time.sleep(0.6)
    driver.set_window_size(size[0], size[1])
    x = driver.get_window_size()["width"]/2
    y = driver.get_window_size()["height"]/1.35
    if debugResolution == True:
        x, y = 250, 275
    debugger(f"X, Y = {x}, {y}")
    debugger(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()
    time.sleep(0.2)
    log("Wait")
    wait_between(MIN_RAND, MAX_RAND)
    debugger(f"Backing")
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
    if debugResolution == True:
        x, y = 245, 185
    debugger(f"X, Y = {x}, {y}")
    debugger(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()

    log("Wait")
    wait_between(MIN_RAND, MAX_RAND)

    window_principal = driver.window_handles[0]
    window_popup = driver.window_handles[1]
    driver.switch_to.window(window_popup)

    log("Wait")
    wait_between(MIN_RAND, MAX_RAND)


    print(driver.current_window_handle)
    driver.switch_to.default_content()
    print(driver.current_window_handle)

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))



    check_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor")))

    action = ActionChains(driver)
    human_like_mouse_move(action, check_box)

    check_box.click()

    log("Wait")
    wait_between(MIN_RAND, MAX_RAND)

    driver.switch_to.default_content()


    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
    time.sleep(0.2)
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='solver-button']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#recaptcha-audio-button"))).click()

    log("Wait")
    wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

    driver.switch_to.window(window_principal)
    time.sleep(0.2)
    driver.switch_to.default_content()

    debugger(f"Backing")
    ActionChains(driver).move_by_offset(-x, -y).click().perform()

    #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        #(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))).click()
    #driver.switch_to.default_content()
    #driver.switch_to.default_content()
    #WebDriverWait(driver, 10).until(
    #    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#solver-button"))).click()
    #driver.switch_to(window_principal)

# Setup proxy
def setUpProxy():
    capabilities['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY
    }
    
def end(force = False): # resets
    found = False
    while not found:
        debugger(f"Waiting for end")
        if force == True:
            debugger(f"Force end")
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
    if debugResolution == True:
        x, y = 140, 250
    debugger(f"X, Y = {x}, {y}")
    debugger(f"Clicking")
    ActionChains(driver).move_by_offset(x, y).click().perform()
    time.sleep(0.2)
    debugger(f"Backing")
    ActionChains(driver).move_by_offset(-x, -y).click().perform()


# Use time.sleep for waiting and uniform for randomizing
def wait_between(a, b):
    rand=uniform(a, b)
    time.sleep(rand)

def human_like_mouse_move(action, start_element):

    points = [[6, 2], [3, 2],[0, 0], [0, 2]];
    points = np.array(points)
    x = points[:,0]
    y = points[:,1]

    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)


    x_tup = si.splrep(t, x, k=1)
    y_tup = si.splrep(t, y, k=1)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    x_i = si.splev(ipl_t, x_list)
    y_i = si.splev(ipl_t, y_list)

    startElement = start_element

    action.move_to_element(startElement)
    action.perform()

    c = 5
    i = 0
    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x,mouse_y);
        action.perform();
        log("Move mouse to, %s ,%s" % (mouse_x, mouse_y))
        i += 1
        if i == c:
            break;


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
    debugger("Sleeping")
    time.sleep(int(s[s.find("mine ")+5:s.find("\"'")])/1000)
    debugger("SleepStop")

debugger("init")
preload()
login()
miner()
mine()
get()
end()
wait()

while True:
    time.sleep(sleeptime())
    mine(True)
    time.sleep(sleeptime()/4)
    get(True)
    end(True)
    wait()
