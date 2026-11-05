from playwright.sync_api import expect
import pytest
import re


PAGE_URL = 'https://the-internet.herokuapp.com/iframe'


def test_heading_is_visible_and_editor_shows_default_text(page):
    page.goto(PAGE_URL)

    expect(page.get_by_role('heading', name='An iFrame containing the TinyMCE WYSIWYG Editor')).to_be_visible()
    expect(page.frame_locator('#mce_0_ifr').locator('#tinymce')).to_have_text('Your content goes here.')


PAGE_URL_TWO = 'https://the-internet.herokuapp.com/nested_frames'

@pytest.mark.parametrize('frame, expected_text', [
    ('[name="frame-left"]', 'LEFT'),
    ('[name="frame-middle"]', 'MIDDLE'),
    ('[name="frame-right"]', 'RIGHT')
], ids=['Top left frame', 'Top middle frame', 'Top right frame'])
def test_each_of_top_frames_shows_its_text(page, frame, expected_text):
    page.goto(PAGE_URL_TWO)

    expect(page.frame_locator('[name="frame-top"]').frame_locator(frame).locator('body')).to_have_text(expected_text)

