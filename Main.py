## Python main class

import function.Core as core
import function.Utils as utils
import time

utils.log("init")
core.preload()
core.login()
core.miner()
core.mine()
core.get()
core.end()
core.wait()

while True:
    time.sleep(utils.random_sleeping())
    core.mine(True)
    time.sleep(utils.random_sleeping()/4)
    core.get(True)
    core.end(True)
    core.wait()
