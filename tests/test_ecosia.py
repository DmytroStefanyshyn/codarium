from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s


def setup_module():
    browser.open('https://www.ecosia.org/')
    browser.driver.maximize_window()


def test_search_and_count_links():
    query = '[name="q"]'
    s(query).type('yashaka selene').press_enter()
    ss('.result-body .js-result-title').first.click()
    ss('[href = "/yashaka/selene"]').should(have.size(3))


def teardown_module():
    browser.close()
