
import numpy as np
import scipy.interpolate as si
import time

import conf.Constants as constants
from random import uniform
from datetime import datetime

def random_sleeping():
    rand = uniform(constants.LONG_MIN_RAND, constants.LONG_MAX_RAND)
    print(f"Going sleep: waiting {rand}s")
    time.sleep(rand)

def human_like_mouse_move(action, start_element):
    points = [[6, 2], [3, 2], [0, 0], [0, 2]];
    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]

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
        action.move_by_offset(mouse_x, mouse_y);
        action.perform();
        log("Move mouse to, %s ,%s" % (mouse_x, mouse_y))
        i += 1
        if i == c:
            break;

def log(t="init"):
    nl = "\n"
    now = datetime.now()

    if t == "init":
        f = open(constants.LOGS_PATH + constants.LOG_FILE_NAME, "w+")
        f.write(f"AWA {constants.ALIENABOT_VERSION} | {datetime.now().strftime('%c')}{nl}")
        f.close()
    else:
        f = open(constants.LOGS_PATH + constants.LOG_FILE_NAME, "a")
        print("%s :: %s " % (str(now), t))
        f.write(f"{datetime.now().strftime('%X')} | {t}{nl}")
        f.close()
