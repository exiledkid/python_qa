import allure

class ProductsPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, product_name):
        with allure.step(title=f'Добавление в корзину товара {product_name}'):
            #пример product_name - sauce-labs-backpack, полное имя будет f'[data-test="add-to-cart-{product_name}"]'
            self.page.locator(f'[data-test="add-to-cart-{product_name}"]').click()

            allure.attach(
                name='Скриншот страницы товара',
                body=self.page.screenshot(),
                attachment_type=allure.attachment_type.PNG
            )

    def get_shopping_cart_counter(self):
        
        return self.page.locator("[data-test='shopping-cart-badge']")

        