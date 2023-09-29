from selene import be, have
from selene.support.shared import browser
import random
import string


def test_random_text_not_found_in_google():
    browser.open('https://google.com')
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
    browser.element('[name="q"]').should(be.blank).type(random_text).press_enter()
    asserted_text = "ничего не найдено"
    assert browser.element('[class="card-section"]').matching(have.text(asserted_text)), \
        f"На случайный запрос '{random_text}' результат поиска не содержит текст '{asserted_text}'"
