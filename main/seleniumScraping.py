import os
import subprocess
import sys
from telnetlib import EC
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_my_list(driver, email, pw, user_profile):
    # go to netflix
    print("Going to Netflix...")
    driver.get("https://www.netflix.com")

    # click login button
    print("Entering Login info")
    current_url = driver.current_url
    login_button = driver.find_element(By.CLASS_NAME, "authLinks redButton")
    login_button.click()
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    # sign in
    current_url = driver.current_url
    email_input = driver.find_element(By.NAME, "userLoginId")
    pw_input = driver.find_element(By.NAME, "password")
    email_input.send_keys(email)
    pw_input.send_keys(pw)

    sign_in_button = driver.find_element(By.CLASS_NAME, "login-button")
    sign_in_button.click()
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    # choose profile by profile name
    print("Choosing your profile")
    profiles = driver.find_elements(By.CLASS_NAME, "profile")
    for profile in profiles:
        name = profile.find_element(By.CLASS_NAME, "profile-name").text
        if name == user_profile:
            profile_link = profile.find_element(By.CLASS_NAME, "profile-link")
            profile_link.click()
            break
    sleep(2)

    # click my list
    print("Finding your list")
    current_url = driver.current_url
    my_list = driver.find_element(By.LINK_TEXT, "My List")
    my_list.click()
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    # scroll down my list to load all titles
    logo = driver.find_element(By.CLASS_NAME, "logo")
    for n in range(1, 10):
        print("Getting list of movies...")
        logo.send_keys(Keys.END)
        sleep(1)

    # return list of movies:
    movies_div = driver.find_elements(By.CLASS_NAME, "title-card")
    movie_titles = [div.find_element(By.CSS_SELECTOR, 'a').get_attribute("aria-label") for div in movies_div]
    driver.quit()
    return movie_titles
