![visitor badge](https://visitor-badge-reloaded.herokuapp.com/badge?page_id=IvanPerez9.ExpiringOnNetflixSoon&color=be54c6&style=flat&logo=Github)
![Manintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![GitHub last commit (master)](https://img.shields.io/github/last-commit/IvanPerez9/ExpiringOnNetflixSoon)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Netflix](https://img.shields.io/badge/Netflix-E50914?style=for-the-badge&logo=netflix&logoColor=white)

# ExpiringOnNetflixSoon

Movies and series from Netflix 'My List' that are going to be removed in the next month.

# Requirements

- Python 3.7 or above
  - Normally required python libraries are configured to install itselft if not run the following command
    ```
    python -m pip install 'package'
    ```
- Webdriver (Chrome webdriver by default)
- UNOGSNG rapid API key

# Installation

- Clone repository
- Create a .env file with the following required fields 
  - EMAIL: Enter your netflix email
  - PASSWORD: Enter your netflix password
  - USER_PROFILE: Enter your profile name
  - API_KEY: Your rapid api free key
  - COUNTRY: Your country code (Ex. ES = Spain; US = United States of America)

![Variables.env](https://github.com/IvanPerez9/ExpiringOnNetflixSoon/blob/main/img/variables.png)


# How to use

- Run main.py file 
- When running it shows two options for users input, 0 and 1
  - Case 0: Get the info from the .env file created before
  - Case 1: Ask for your email, password, user profile and country

- When finish it will show a list of shows and films that are about to expired or if you are lucky it will display a message saying that you have nothing that is about to expire.
