class DynamicControlsPage:
    SITE_URL = 'https://the-internet.herokuapp.com/dynamic_controls'

    def __init__(self, page):
        self.page = page

    def open_page(self):
        self.page.goto(self.SITE_URL)

    def press_remove_button(self):
        self.page.get_by_role('button', name='Remove').click()

    def press_add_button(self):
        self.page.get_by_role('button', name='Add').click()

    def press_enable_button(self):
        self.page.get_by_role('button', name='Enable').click()

    def press_disable_button(self):
        self.page.get_by_role('button', name='Disable').click()

    def get_checkbox(self):
        return self.page.get_by_role('checkbox')

    def get_input_field(self):
        return self.page.get_by_role('textbox')

    def get_checkbox_message(self):
        return self.page.locator('#checkbox-example').locator('#message')

    def get_input_message(self):
        return self.page.locator('#input-example').locator('#message')

    def enter_text(self, text):
        self.page.get_by_role('textbox').fill(text)
