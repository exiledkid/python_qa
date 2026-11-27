import allure
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def fill_info(self, first_name, last_name, postal_code):
        with allure.step(title='Процесс заполнения данных'):
            self.page.locator('[data-test="firstName"]').fill(first_name)
            self.page.locator('[data-test="lastName"]').fill(last_name)
            self.page.locator('[data-test="postalCode"]').fill(postal_code)

            self.page.locator('[data-test="continue"]').click()

    def get_error(self):
        return self.page.locator('[data-test="error"]')
