import allure
class LoginPage():
    def __init__(self, page):
        self.page = page

    def open(self):
        with allure.step(title='Вход на сайт'):
            self.page.goto('https://www.saucedemo.com')

    def login(self, username, password):
        with allure.step(title=f'Авторизация на сайте, пользователь {username}'):
            self.page.get_by_placeholder('Username').fill(username)
            self.page.get_by_placeholder('Password').fill(password)
            self.page.get_by_role('button', name='Login').click()

            allure.attach(
                body=self.page.screenshot(),
                name='Страница после нажатия Login',
                attachment_type=allure.attachment_type.PNG
            )

    