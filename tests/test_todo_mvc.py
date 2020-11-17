from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s


def setup_module():
    browser.open('http://todomvc.com/examples/emberjs/')
    browser.driver.maximize_window()


def test_adding_and_completing_tasks():
    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()
    ss('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    s('#todo-list>li:nth-child(2) .toggle').click()
    s('#todo-list>li:nth-child(2)').should(have.css_class('completed'))
    s('#todo-list>li:nth-child(1)').should(have.no.css_class('completed'))
    s('#todo-list>li:nth-child(3)').should(have.no.css_class('completed'))


def teardown_module():
    browser.close()
