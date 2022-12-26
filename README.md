![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FIvanPerez9%2FExpiringOnNetflixSoon&countColor=%23ff8a65&style=flat&labelStyle=none)
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=9cf&label=Clone&query=count&url=https://gist.githubusercontent.com/IvanPerez9/59a5b3a0369b18a33e49c05830481acf/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)
![Manintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![GitHub last commit (master)](https://img.shields.io/github/last-commit/IvanPerez9/ExpiringOnNetflixSoon)
[![Custom Deployment](https://github.com/IvanPerez9/ExpiringOnNetflixSoon/actions/workflows/cloneCountAction.yml/badge.svg)](https://github.com/IvanPerez9/ExpiringOnNetflixSoon/actions/workflows/cloneCountAction.yml)


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Netflix](https://img.shields.io/badge/Netflix-E50914?style=for-the-badge&logo=netflix&logoColor=white)


# ExpiringOnNetflixSoon

Movies and series from Netflix 'My List' that are going to be removed in the next month.

 ---
# 💻 Requirements

- Python 3.7 or above
  - Normally required python libraries are configured to install themselves if not, run the following command
    ```
    python -m pip install 'package'
    ```
- Webdriver (Chrome webdriver by default)
- UNOGSNG rapid API key

# ⚙️ Installation

- Clone repository
- Create a .env file with the following required fields 
  - EMAIL: Enter your netflix email
  - PASSWORD: Enter your netflix password
  - USER_PROFILE: Enter your profile name
  - API_KEY: Your rapid api free key
  - COUNTRY: Your country code (Ex. ES = Spain; US = United States of America)

![Variables.env](https://github.com/IvanPerez9/ExpiringOnNetflixSoon/blob/main/img/variables.png)


# 📖 How to use

- Run main.py file 
- When running, it shows two options for users input, 0 and 1
  - Case 0: Get the info from the .env file created before
  - Case 1: It ask for your Netflix email, password, user profile and country

- When completed, it will show a list of shows and films that are about to expire or if you are lucky it will display a message informing that you have nothing that is about to expire.
