from playwright.sync_api import expect
from pathlib import Path

UPLOAD_FILE = Path(__file__).parent / 'data' / 'upload_test.txt'

def test_upload(page):
    page.goto('https://the-internet.herokuapp.com/upload')
    page.locator('#file-upload').set_input_files(UPLOAD_FILE)
    page.locator('#file-submit').click()

    expect(page.locator('#uploaded-files')).to_have_text('upload_test.txt')