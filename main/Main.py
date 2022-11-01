import os
import subprocess
import sys

from selenium import webdriver
from SeleniumScraping import get_my_list
from GetExpiringPerCountry import get_expiring_per_country

email = None
pw = None
user_profile = None
country = None
api_key = None

def pipinstall(package):
    '''
    Function to install packages
    @param package:
    @return:
    '''
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def readDefaultAccountFromFileOrLoadNewAccount ():
    '''
    Select default account or enter a new one to extract 'My list' information
    @return: email, password, user, country and api key to global variables
    '''
    # ------- Env variables ------------
    pipinstall("python-dotenv")
    from dotenv import load_dotenv

    # Get the path to the directory this file is in
    BASEDIR = os.path.abspath(os.path.dirname("variables.env"))
    # Connect the path with your '.env' file name
    load_dotenv(os.path.join(BASEDIR, 'variables.env'))

    account = input("Choose default account store in .env (0) or enter a new one (1): ")
    global email
    global pw
    global user_profile
    global country
    global api_key

    # Your rapid api free key
    api_key = os.getenv("API_KEY")

    if account == '0':
        # enter your Netflix email
        email = os.getenv('EMAIL')
        # enter your Netflix password
        pw = os.getenv("PASSWORD")
        # enter your profile name
        user_profile = os.getenv("USER_PROFILE")
        # Change your country code (see readme for list of countries)
        country = os.getenv("COUNTRY")
    elif account == '1':
        email = input("Enter your Netflix email account: ")
        pw = input("Enter your Netflix password account: ")
        user_profile = input("Enter your user profile name: ")
        country = input("Enter you country: (Ex: ES for Spain or US for USA) ")
    else:
        print("Please enter a valid option")
        readDefaultAccountFromFileOrLoadNewAccount()



if __name__ == '__main__':
    # ----------- Install webdriver ------------
    pipinstall("webdriver-manager")
    pipinstall("chromedriver_binary")

    # Chrome driver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    # headless not show selenium running
    options = Options()
    #options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # ---------- select account --------
    readDefaultAccountFromFileOrLoadNewAccount()
    # ------- seleniumScraping ---------
    my_list_titles = get_my_list(driver=driver, email=email, pw=pw, user_profile=user_profile)
    # ------- API expiring movies ------
    expiring_movies = get_expiring_per_country(country=country, api_key=api_key)

    my_expiring_movies = {}
    for movie in expiring_movies:
        if movie in my_list_titles:
            my_expiring_movies[movie] = expiring_movies[movie]

    if len(my_expiring_movies) > 0:
        print("------------------------------------------")
        print("EXPIRING: ")
        print(my_expiring_movies)
        print("------------------------------------------")
    else:
        print("------------------------------------------")
        print("Nothing from your list is about to expire.")
        print("------------------------------------------")
