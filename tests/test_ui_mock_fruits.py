from playwright.sync_api import expect
import pytest

PAGE_URL = 'https://demo.playwright.dev/api-mocking/'
FRUITS_API_URL = 'https://demo.playwright.dev/api-mocking/api/v1/fruits'


def test_page_shows_mocked_fruit(page):
    page.route(FRUITS_API_URL, lambda route: route.fulfill(json=[{'name': 'Mockingbird', 'id': 1337}]))
    page.goto(PAGE_URL)

    expect(page.get_by_text('Mockingbird')).to_be_visible()
    expect(page.get_by_text('Strawberry')).not_to_be_visible()


@pytest.mark.xfail(reason='Page does not handle 500 server error: infinite loading')
def test_hides_loading_on_server_error(page):
    page.route(FRUITS_API_URL, lambda route: route.fulfill(status=500))
    page.goto(PAGE_URL)

    expect(page.get_by_text('Loading...')).not_to_be_visible()
