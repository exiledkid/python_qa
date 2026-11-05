from playwright.sync_api import expect
from pathlib import Path


FILE_PATH = Path(__file__).parent / 'data' / 'my_very_unique_file.txt'


def test_success_upload_confirmation_is_visible(page):

    page.goto('https://the-internet.herokuapp.com/upload')
    page.locator('#file-upload').set_input_files(FILE_PATH)
    page.locator('#file-submit').click()

    expect(page.locator('.example')).to_contain_text('File Uploaded!')
    expect(page.locator('#uploaded-files')).to_have_text(FILE_PATH.name)



def test_downloaded_file_text_and_name_is_same_as_ours(page):
    page.goto('https://the-internet.herokuapp.com/download')

    with page.expect_download() as download_info:
        page.get_by_role('link', name=FILE_PATH.name).click()

    assert download_info.value.suggested_filename == FILE_PATH.name

    download_text = download_info.value.path().read_text()
    assert download_text == FILE_PATH.read_text()
