import pytest
import re
from playwright.sync_api import expect

def test_login_success(login_page, products_page, page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')

    expect(page).to_have_url(re.compile('inventory'))
    expect(products_page.get_title()).to_be_visible()
    expect(products_page.get_inventory_items()).to_have_count(6)
    expect(products_page.get_title()).to_have_text('Products')



# ТЕСТ 2 — неудачный вход, одним тестом на все случаи (parametrize)
@pytest.mark.parametrize('login, password, exp_error', [
    ('standard_user', 'standard_password', 'Epic sadface: Username and password do not match any user in this service'),
    ('', 'secret_sauce', 'Epic sadface: Username is required'),
    ('standard_user', '', 'Epic sadface: Password is required'),
    ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.')
], ids=['Incorrect password', 'Incorrect login', 'Password required', 'Blocked user'])
def test_auth_fail(login_page, page, login, password, exp_error):
    login_page.open()
    login_page.login(login, password)

    expect(login_page.get_error()).to_be_visible()
    expect(login_page.get_error()).to_have_text(exp_error)
    expect(page).not_to_have_url(re.compile('inventory'))