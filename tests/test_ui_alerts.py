from playwright.sync_api import expect
def test_click_for_confirm(page):
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    page.once('dialog', lambda dialog: dialog.accept())
    page.get_by_role('button', name='Click for JS Confirm').click()

    expect(page.locator('#result')).to_have_text('You clicked: Ok')

def test_click_for_prompt(page):
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    page.once('dialog', lambda dialog: dialog.accept('Nikita'))
    page.get_by_role('button', name='Click for JS Prompt').click()
    expect(page.locator('#result')).to_contain_text('Nikita')