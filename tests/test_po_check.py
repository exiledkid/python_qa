from playwright.sync_api import expect
from pages.login_page import LoginPage
import re

def test_login_page(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
    expect(page).to_have_url(re.compile('inventory'))