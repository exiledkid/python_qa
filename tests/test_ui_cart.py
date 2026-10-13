from playwright.sync_api import expect

def test_add_item_to_cart_success(login_page, products_page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')

    products_page.add_to_cart('sauce-labs-backpack')

    expect(products_page.get_shopping_cart_counter()).to_have_text('1')
        
