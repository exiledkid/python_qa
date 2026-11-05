import pytest
from playwright.sync_api import expect


PAGE_URL = 'https://demo.playwright.dev/api-mocking/'
FRUITS_API = 'https://demo.playwright.dev/api-mocking/api/v1/fruits'
FRUIT_NAME = 'Applenana'

def request_handler(route):
    fruits = [{'name': 'Apple v2.0', 'id': 998}, {'name': 'Banana v2.0', 'id': 999}]

    route.fulfill(json=fruits)


def test_fully_mocked_fruit_list(page):
    page.route(FRUITS_API, request_handler)
    page.goto(PAGE_URL)

    expect(page.get_by_text('Apple v2.0')).to_be_visible()
    expect(page.get_by_text('Banana v2.0')).to_be_visible()
    expect(page.get_by_text('Strawberry')).not_to_be_visible()


def request_handler_two(route):
    response = route.fetch()
    response_list = response.json()

    response_list[0]['name'] = FRUIT_NAME

    route.fulfill(response=response, json=response_list)


def test_fruit_name_modified(page):
    page.route(FRUITS_API, request_handler_two)
    page.goto(PAGE_URL)

    expect(page.get_by_text(FRUIT_NAME)).to_be_visible()


@pytest.mark.xfail(reason='Loading is still visible on the page despite server status 500')
def test_server_error_500(page):
    page.route(FRUITS_API, lambda route: route.fulfill(status=500))
    page.goto(PAGE_URL)

    expect(page.get_by_text('Loading...')).not_to_be_visible()
