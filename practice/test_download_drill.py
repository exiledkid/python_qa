def test_download_first_file(page):
    page.goto('https://the-internet.herokuapp.com/download')

    link = page.locator('.example a').first

    file_name = link.text_content()

    with page.expect_download() as download_info:
        link.click()

    download_file = download_info.value

    assert download_file.suggested_filename == file_name

