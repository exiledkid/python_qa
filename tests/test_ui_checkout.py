from playwright.sync_api import expect
import re
import pytest

def test_full_cycle(page, login_page, products_page, cart_page, checkout_step_one_page, checkout_step_two_page, checkout_complete_page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')

    products_page.add_to_cart('sauce-labs-backpack')
    expect(products_page.get_shopping_cart_counter()).to_have_text('1')
    products_page.open_cart()

    expect(page).to_have_url(re.compile('cart'))

    expect(cart_page.get_product_name()).to_have_text('Sauce Labs Backpack')
    expect(cart_page.get_product_price()).to_have_text('$29.99')
    cart_page.checkout()

    expect(page).to_have_url(re.compile('checkout-step-one'))

    checkout_step_one_page.fill_info('Alex', 'Verder', '444213')

    expect(page).to_have_url(re.compile('checkout-step-two'))

    expect(checkout_step_two_page.get_product_name()).to_have_text('Sauce Labs Backpack')
    expect(checkout_step_two_page.get_product_price()).to_have_text('$29.99')
    checkout_step_two_page.finish()

    expect(page).to_have_url(re.compile('checkout-complete'))

    expect(checkout_complete_page.get_order_result()).to_contain_text('dispatched')

@pytest.mark.parametrize('first_name, last_name, postal_code, expected_error', [
    ('', 'Alexandrov', '222', 'Error: First Name is required'),
    ('Alex', '', '222', 'Error: Last Name is required'),
    ('Alex', 'Alexandrov', '', 'Error: Postal Code is required')
],
ids=['Empty First Name', 'Empty Last Name', 'Empty Postal Code']
)
def test_step_one_info_fail(page, login_page, products_page, cart_page, checkout_step_one_page, 
    first_name, last_name, postal_code, expected_error):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')

    products_page.add_to_cart('sauce-labs-backpack')
    products_page.open_cart()

    expect(page).to_have_url(re.compile('cart'))

    cart_page.checkout()

    expect(page).to_have_url(re.compile('checkout-step-one'))
    checkout_step_one_page.fill_info(first_name, last_name, postal_code)

    expect(checkout_step_one_page.get_error()).to_be_visible()
    expect(checkout_step_one_page.get_error()).to_have_text(expected_error)

    expect(page).to_have_url(re.compile('checkout-step-one'))
