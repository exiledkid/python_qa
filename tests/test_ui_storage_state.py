from playwright.sync_api import expect
import re


def test_verify_restored_authentication_and_context_isolation(page, browser, login_page):

    context = None
    unauth_context = None

    try:

        login_page.open()

        login_page.login('standard_user', 'secret_sauce')

        expect(page).to_have_url(re.compile('inventory'))

        new_page = page.context.new_page()

        assert new_page.context is page.context

        page.context.storage_state(path='playwright/.auth/user.json')

        context = browser.new_context(storage_state='playwright/.auth/user.json')
        new_page_2 = context.new_page()

        assert new_page_2.context is not page.context

        new_page_2.goto('https://www.saucedemo.com/cart.html')

        expect(new_page_2).to_have_url(re.compile('cart'))

        unauth_context = browser.new_context()
        new_page_3 = unauth_context.new_page()

        new_page_3.goto('https://www.saucedemo.com/cart.html')

        expect(new_page_3).to_have_url('https://www.saucedemo.com/')

    finally:
        if context is not None:
            context.close()

        if unauth_context is not None:
            unauth_context.close()
