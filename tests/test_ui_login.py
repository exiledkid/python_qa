import pytest
import re
from playwright.sync_api import expect

def test_login_success(page):
    page.goto('https://www.saucedemo.com/')

    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_role('Button', name='login').click()

    expect(page).to_have_url(re.compile('inventory'))
    expect(page.locator('[data-test="title"]')).to_be_visible()
    expect(page.locator('[data-test="inventory-item"]')).to_have_count(6)
    expect(page.locator('[data-test="title"]')).to_have_text('Products')



# ТЕСТ 2 — неудачный вход, одним тестом на все случаи (parametrize)
@pytest.mark.parametrize('login, password, exp_error', [
    ('standard_user', 'standard_password', 'Epic sadface: Username and password do not match any user in this service'),
    ('', 'secret_sauce', 'Epic sadface: Username is required'),
    ('standard_user', '', 'Epic sadface: Password is required'),
    ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.')
], ids=['Неверный пароль', 'Нет логина', 'Нет пароля', 'Заблокированный пользователь'])
def test_auth_fail(page, login, password, exp_error):
    page.goto('https://www.saucedemo.com/')

    page.get_by_placeholder('Username').fill(login)
    page.get_by_placeholder('Password').fill(password)
    page.get_by_role('Button', name='login').click()

    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_have_text(exp_error)