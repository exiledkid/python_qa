import allure

class CheckoutStepTwoPage:
    def __init__(self, page):
        self.page = page

    def get_product_name(self):
        return self.page.locator('[data-test="inventory-item-name"]')
    
    def get_product_price(self):
        return self.page.locator('[data-test="inventory-item-price"]') 
    
    def finish(self):
        with allure.step(title='Нажатие кнопки Finish'):
            self.page.locator('[data-test="finish"]').click()