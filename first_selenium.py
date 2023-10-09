
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def browser():
    # Open browser
    driver = webdriver.Chrome()  # Или любой другой браузер
    yield driver   # передаём в функцию, которой вызываем фикстуру
    # Close the browser
    driver.quit()


def test_verify_title(browser):
    # Navigate to the website
    browser.get("https://sdetunicorns.com")

    # Get the title of the page
    title = browser.title

    # Verify the title
    expected_title = "Master Software Testing and Automation | SDET Unicorns"
    assert title == expected_title




def test_login_to_item_card_irisamo(browser):
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    time.sleep(1)
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    time.sleep(1)
    browser.find_element(By.ID, 'login-button').click()
    time.sleep(1)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'

