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


@pytest.mark.xfail(reason='Page does not handle no response from server: infinite loading')
def test_hides_loading_on_network_error(page):
    page.route(FRUITS_API_URL, lambda route: route.abort())
    page.goto(PAGE_URL)

    expect(page.get_by_text('Loading...')).not_to_be_visible()


def add_fruit_to_response(route):
    response = route.fetch()
    response_data = response.json()
    fruit = {'name': 'Veryberry', 'id': 228}
    response_data.append(fruit)
    route.fulfill(response=response, json=response_data)


def test_page_shows_real_and_added_fruit(page):
    page.route(FRUITS_API_URL, add_fruit_to_response)
    page.goto(PAGE_URL)

    expect(page.get_by_text('Veryberry')).to_be_visible()
    expect(page.get_by_text('Strawberry')).to_be_visible()
