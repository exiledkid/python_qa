from playwright.sync_api import expect
import pytest
import re


class LoginPage():
    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto('https://the-internet.herokuapp.com/login')

    def login(self, login, password):
        self.page.get_by_label('Username').fill(login)
        self.page.get_by_label('Password').fill(password)

        self.page.get_by_role('button', name='Login').click()

    def get_login_message(self):
        return self.page.locator('#flash')

    def get_logout_link(self):
        return self.page.get_by_role('link', name='Logout')

@pytest.fixture
def login_page(page):
    return LoginPage(page)


# 4. Вопросы (ответ словами):
#    a) почему методы для плашки и Logout делают return, а не print?
# ответ - чтобы вернуть в место вызова локатор, а не напечатать его в терминале. с ним потом идет проверка
#    b) в тесте ты вызываешь метод, который возвращает локатор, и передаёшь результат в expect.
#
#       Где нужны скобки: у имени метода? у expect? Почему?
# ответ - у метода и у экспект, оба выполняют действие
# 5. «Сломай и проверь»: испорти локатор плашки в КЛАССЕ (одно место).
#    Должны упасть оба теста. Это и есть польза Page Object.
#
# ПРИСЛАТЬ: код + зелёный прогон с -v + падение после поломки + ответы на п. 4.



def test_successful_login_text_and_logout_link_are_visible_after_login(page, login_page):
    login_page.open_page()
    login_page.login('tomsmith', 'SuperSecretPassword!')

    expect(page).to_have_url(re.compile('secure'))
    expect(login_page.get_login_message()).to_contain_text('You logged into a secure area!')
    expect(login_page.get_logout_link()).to_be_visible()


@pytest.mark.parametrize('login, password, expected_error_text',[
    ('alexsmith', 'SuperSecretPassword!', 'Your username is invalid!'),
    ('tomsmith', 'pass1', 'Your password is invalid!'),
    ('', '', 'Your username is invalid!')
], ids=['Wrong login, correct password', 'Correct login, wrong password', 'Empty login and password'])
def test_error_during_login_using_incorrect_data(page, login, password, expected_error_text, login_page):
    login_page.open_page()
    login_page.login(login, password)

    expect(login_page.get_login_message()).to_contain_text(expected_error_text)
    expect(page).not_to_have_url(re.compile('secure'))
