from playwright.sync_api import expect


def test_page_shows_mocked_fruit(page):
    page.route('https://demo.playwright.dev/api-mocking/api/v1/fruits', lambda route: route.fulfill(json=[{'name': 'Mockingbird', 'id': 1337}]))
    page.goto('https://demo.playwright.dev/api-mocking/')

    expect(page.get_by_text('Mockingbird')).to_be_visible()
    expect(page.get_by_text('Strawberry')).not_to_be_visible()
