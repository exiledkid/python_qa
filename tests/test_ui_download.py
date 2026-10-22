def test_download(page):
    page.goto('https://the-internet.herokuapp.com/download')
    link = page.locator('.example a').last
    file_name = link.text_content()

    with page.expect_download() as download_info:
        link.click()

    downloaded_file = download_info.value

    assert downloaded_file.suggested_filename == file_name