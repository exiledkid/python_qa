from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    def get_product_name(self):
        return self.page.locator('[data-test="cart-list"]').locator('[data-test="inventory-item-name"]')

    def get_product_price(self):
        return self.page.locator('[data-test="cart-list"]').locator('[data-test="inventory-item-price"]')

    def checkout(self):
        with allure.step(title='Нажатие кнопки Checkout'):
            self.page.locator('[data-test="checkout"]').click()
