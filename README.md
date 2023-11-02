# Sophos Bits Internet Auto-Login

Simple python script I made using Selenium for logging in to the Lan/wifi provided at BPHC.

# Required Setup

```
pip install -r requirements.txt
```

Download the version of [chromedriver](https://chromedriver.chromium.org/downloads) that matches with the version of your chrome on your device (in the Chrome menu, go to 'Help' and then 'About Google Chrome' to see the version of chrome on your device), for your OS. Then extract the downloaded zip file and copy and paste the .exe file to the scripts folder inside the folder where python is installed in your system, or just add the .exe file to PATH directly.

# Usage Instructions

Make a .env file in the same directory as this script, and enter your username, password, and the url of the login page in that file, in the following format:
```
sophos_username=your_username_here
sophos_password=your_password_here
login_url=url_of_the_login_page
```