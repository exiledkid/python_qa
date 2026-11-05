from playwright.sync_api import expect
import pytest
import re


PAGE_URL = 'https://the-internet.herokuapp.com/javascript_alerts'


def accept_dialog(dialog):
    dialog.accept()


def test_page_shows_ok_click_confirmation_after_dialog(page):
    page.once('dialog', accept_dialog)
    page.goto(PAGE_URL)
    page.get_by_role('button', name='Click for JS Confirm').click()


    expect(page.locator('#result')).to_have_text('You clicked: Ok')



def test_page_shows_cancel_click_confirmation_after_dialog(page):
    page.once('dialog', lambda dialog: dialog.dismiss())
    page.goto(PAGE_URL)
    page.get_by_role('button', name='Click for JS Confirm').click()

    expect(page.locator('#result')).to_have_text('You clicked: Cancel')


def test_page_shows_entered_text_after_dialog(page):
    page.once('dialog', lambda dialog: dialog.accept('My text'))
    page.goto(PAGE_URL)
    page.get_by_role('button', name='Click for JS Prompt').click()

    expect(page.locator('#result')).to_have_text('You entered: My text')
