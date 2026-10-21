from playwright.sync_api import expect
def test_iframe(page):
    page.goto('https://the-internet.herokuapp.com/iframe')
    expect(page.frame_locator('#mce_0_ifr').locator('#tinymce')).to_have_text('Your content goes here.')