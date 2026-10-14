import allure

class CheckoutStepOnePage:
    def __init__(self, page):
        self.page = page

    def fill_info(self, first_name, last_name, postal_code):
        with allure.step(title='Процесс заполнения данных'):
            self.page.locator('[data-test="firstName"]').fill(first_name)
            self.page.locator('[data-test="lastName"]').fill(last_name)
            self.page.locator('[data-test="postalCode"]').fill(postal_code)
            
            self.page.locator('[data-test="continue"]').click()

    def get_error(self):
        return self.page.locator('[data-test="error"]')