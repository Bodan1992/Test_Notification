from selene.support.shared import browser
from selene import be, have

from selenium import webdriver

browser.config.driver = webdriver.Chrome()


def test_search():
    browser.open('https://www.google.com/')
    browser.element('[name="q"]').should(be.blank).type('Selene - Web UI browser in Python').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))




