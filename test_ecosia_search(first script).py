from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser

# Given
browser.open('https://www.ecosia.org/')

# When
s('[name="q"]').type('yashaka selene').press_enter()
ss('.result-body .js-result-title').first.click()

# Then
ss('[href = "/yashaka/selene"]').should(have.size(3))
