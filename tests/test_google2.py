from selene import be, have


def test_search_valid(setup_browser):
    browser = setup_browser
    browser.open('https://www.ecosia.org/')
    browser.element('[name="q"]').should(be.blank).type('Selene - Web UI browser in Python').press_enter()
    browser.element('[data-test-id="mainline"]').should(have.text("User-oriented Web UI browser tests in Python - GitHub"))


def test_search_invalid(setup_browser):
    browser = setup_browser
    browser.element('[name="q"]').should(be.blank).type('SeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSadasdsad5q4w4qww4eSeSeSeSeSeSeSeSeSev').press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(have.text("Yikes! We didn't find any results for “SeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSadasdsad5q4w4qww4eSeSeSeSeSeSeSeSeSev”"))
