from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def get_order_result(self):
        return self.page.locator('[data-test="complete-text"]')
