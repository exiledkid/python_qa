class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page

    def get_order_result(self):
        return self.page.locator('[data-test="complete-text"]')