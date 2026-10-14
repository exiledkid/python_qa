import allure

class ProductsPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, product_name):
        with allure.step(title=f'Добавление в корзину товара {product_name}'):
            self.page.locator(f'[data-test="add-to-cart-{product_name}"]').click()
            
            allure.attach(
                body=self.page.screenshot(),
                name='Страница после добавления товара в корзину',
                attachment_type=allure.attachment_type.PNG
            )


    def get_shopping_cart_counter(self):
        return self.page.locator('[data-test="shopping-cart-badge"]')

    def open_cart(self):
        with allure.step(title='Нажатие на корзину'):
            self.page.locator('[data-test="shopping-cart-link"]').click()
    
