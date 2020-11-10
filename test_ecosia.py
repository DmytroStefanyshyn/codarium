from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser

browser.open("https://www.ecosia.org/")
s('[data-test-id="search-form-input"]').type('yashaka selene').press_enter()
s('[class="card-desktop card-web"] > div:first-child').click()
ss('[href="/yashaka/selene"]').should(have.size(3))
