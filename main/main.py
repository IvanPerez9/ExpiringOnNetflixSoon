import os
import subprocess
import sys

from selenium import webdriver
from seleniumScraping import get_my_list
from GetExpiringPerCountry import get_expiring_per_country


def pipinstall(package):
    '''
    Function to install packages
    @param package:
    @return:
    '''
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


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

    # ------- Env variables ------------
    pipinstall("python-dotenv")
    from dotenv import load_dotenv, dotenv_values

    load_dotenv(".env")
    config = dotenv_values(".env")
    print(config["EMAIL"])

    # enter your Netflix email
    email = os.getenv('EMAIL')
    # enter your Netflix password
    pw = os.getenv("PASSWORD")
    # enter your profile name
    user_profile = os.getenv("USER_PROFILE")
    # enter your rapid api key (it's free)
    api_key = os.getenv("API_KEY")
    # Change your country code (see readme for list of countries)
    country = os.getenv("COUNTRY")

    # ------- seleniumScraping ---------
    my_list_titles = get_my_list(driver=driver, email=email, pw=pw, user_profile=user_profile)
    # ------- API expiring movies ------
    expiring_movies = get_expiring_per_country(country=country, api_key=api_key)

    my_expiring_movies = {}
    for movie in expiring_movies:
        if movie in my_list_titles:
            my_expiring_movies[movie] = expiring_movies[movie]

    if len(my_expiring_movies) > 0:
        print(my_expiring_movies)
    else:
        print("Nothing is about to expire.")
