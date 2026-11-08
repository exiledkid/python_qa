from playwright.sync_api import expect
import re


def test_new_tab_opens_after_clicking_the_link(page):
    page.goto('https://the-internet.herokuapp.com/windows')

    with page.context.expect_page() as new_page_info:
        page.get_by_role('link', name='Click here').click()

    new_page = new_page_info.value

    expect(new_page).to_have_url(re.compile('/windows/new'))
    expect(new_page.get_by_role('heading')).to_have_text('New Window')

    expect(page.get_by_role('heading')).to_have_text('Opening a new window')


def test_entry_ad_modal_appears_on_load_and_disappears_after_closing(page):
    page.goto('https://the-internet.herokuapp.com/entry_ad')

    expect(page.locator('.modal').get_by_role('heading')).to_have_text('This is a modal window')

    page.locator('.modal-footer').get_by_text('Close').click()

    expect(page.locator('.modal')).not_to_be_visible()
