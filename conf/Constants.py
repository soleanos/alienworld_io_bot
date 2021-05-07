# files path
LOGS_PATH = "./log/"

#URLS
WAX_WALLET_LOGIN_URL = "https://wallet.wax.io/"
WAX_WALLET_DASHBOARD_URL = "https://wallet.wax.io/dashboard"
REDDIT_URL = "https://www.reddit.com/"
ALIENWORD_URL = "https://play.alienworlds.io/"
# ANTICAPTCHA_LOGIN_URL = "https://all-access.wax.io/cloud-wallet/signing/"
ANTICAPTCHA_LOGIN_URL = "https://public-wax-on.wax.io/wam/sign"
ANTICAPTCHA_SITEKEY = "6LdaB7UUAAAAAD2w3lLYRQJqsoup5BsYXI2ZIpFF"

## Sleeping constants
MIN_RAND = 0.64
MAX_RAND = 1.27
LONG_MIN_RAND = 4.78
LONG_MAX_RAND = 11.1

LOG_FILE_NAME = "debug.log"
ALIENABOT_VERSION = "1.3"
DEBUG_RESOLUTION = True
DEBUG_BARS_ADD = 0


## Proxy for preventing to be detected as a bot
PROXIES =[
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
