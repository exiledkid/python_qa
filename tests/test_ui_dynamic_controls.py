from playwright.sync_api import expect


def test_checkbox_not_visible_when_deleted_and_message_appears(dynamic_controls_page):
    dynamic_controls_page.open_page()
    dynamic_controls_page.press_remove_button()

    expect(dynamic_controls_page.get_checkbox_message()).to_have_text("It's gone!")
    expect(dynamic_controls_page.get_checkbox()).not_to_be_visible()


def test_checkbox_visible_after_deleting_and_turning_back_and_message_appears(dynamic_controls_page):
    dynamic_controls_page.open_page()
    dynamic_controls_page.press_remove_button()
    dynamic_controls_page.press_add_button()

    expect(dynamic_controls_page.get_checkbox_message()).to_have_text("It's back!")
    expect(dynamic_controls_page.get_checkbox()).to_be_visible()



def test_input_is_available_when_enabled_and_message_appears(dynamic_controls_page):
    text = 'Text test 123'

    dynamic_controls_page.open_page()
    dynamic_controls_page.press_enable_button()

    expect(dynamic_controls_page.get_input_message()).to_have_text("It's enabled!")
    expect(dynamic_controls_page.get_input_field()).to_be_enabled()

    dynamic_controls_page.enter_text(text)

    expect(dynamic_controls_page.get_input_field()).to_have_value(text)


def test_input_disabled_after_turning_on_and_off(dynamic_controls_page):
    dynamic_controls_page.open_page()
    dynamic_controls_page.press_enable_button()
    dynamic_controls_page.press_disable_button()

    expect(dynamic_controls_page.get_input_message()).to_have_text("It's disabled!")
    expect(dynamic_controls_page.get_input_field()).to_be_disabled()
