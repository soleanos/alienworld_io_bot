---
##### Alienabot was made for educational purposes only, the developers and contributors do not take any responsibility for your WAX.io, AlienWorlds and, or Reddit accounts.
##### Based on technical socle [alienworldsauto](https://github.com/anonieX/alienworldsauto)  
 who doesnt manage captcha; is detected as bot and not work with atual popups
---

### Requirements
- Python 3.7 or greater
- Brave browser
- Chromedriver
- Installed requiremets.txt
- A Reddit account
- A Wax.io account created using your Reddit

---
## Instalation guide
### Install Python and modules
*Skip this if you already have Python an the required modules installed*
1. Install [Python](https://www.python.org/downloads/release/python-378/). 
2. Go at projet root 
3. Use Pip install -r requierment.txt, this will install all you need 

### Config edits
5. Edit the `reddit_username` and `reddit_password` values in main.py to match your Reddit login
### Account creation
7. Create a wax account with your Reddit here: https://all-access.wax.io/
8. Create your AlienWorlds account here: https://play.alienworlds.io/
9. Run Alienworld one time and accept all first transactions, configure ur items and mining map
### Dependency installation
10. Install brave browser in the default directory
11. Install ChromeDriver in your C:/Driver/chromedriver.exe directory from here: https://chromedriver.chromium.org/downloads
### Finishing!
13. Start the script by running main.py!
14. Do not resize the window.
15. Have fun!


### For your information
I don't want this project to be used by too many people and ruin the user experience of the Alienworld site.    
This is why I will not make available on this repo the latest version of the project which is fully functional,  
passes the captchas in an undetectable way and transmits notifications on telegram or teams.  
You can however use the base as I myself used the base of the project  [alienworldsauto](https://github.com/anonieX/alienworldsauto)      
to develop the missing parts: I left here the links which I used to make the code operational.    
For your information solution is based on a paid service (about 1 or 2 dollars for 1000 captcha spent)  
However, i reserve the right to agree to give the missing files to trusted persons who will contact me in exchange of small donation in cryptocurrency.   

### Sources 
[bypass with proxy](https://github.com/teal33t/captcha_bypass/blob/12cd04b3a66a11704bc6da610964ffe01fa06856/recaptcha_buster_bypass.py#L98)  
[js bot](https://gist.github.com/pich4ya/2f20e4b8126d1539a355cbefac3aafb8)  
[anti captcha](https://anti-captcha.com/mainpage)  
[2captcha python lib solver](https://pypi.org/project/decaptcher/)  
[selenium python socle](https://github.com/anonieX/alienworldsauto)  
[code audio captcha solver](https://github.com/FbarcalaR/Boxing-Bouts-Predictor/blob/056be7beb2fc1c9eda9c27ee9f1ce868ebb255c6/boxing_prediction_project/boxing_prediction_project/recaptcha_v2_solver.py)  
[decaptcha solver python lib](https://pypi.org/project/decaptcha/)  
[prevent bot python lib detection](https://github.com/ultrafunkamsterdam/undetected-chromedriver)  
[anti captcha celenium implementation]( https://github.com/ad-m/python-anticaptcha/blob/master/examples/recaptcha_selenium.py)  
[prevent antibot slack](https://stackoverflow.com/questions/53039551/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detec/53040904#53040904)