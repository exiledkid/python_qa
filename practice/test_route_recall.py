from playwright.sync_api import expect

PAGE_URL = 'https://demo.playwright.dev/api-mocking/'
FRUITS_API = 'https://demo.playwright.dev/api-mocking/api/v1/fruits'


def request_handler(route):
    print(route.request.url)
    print(route.request.method)
    route.continue_()


def test_displays_strawberry_when_request_unchanged(page):
    page.route(FRUITS_API, request_handler)
    page.goto(PAGE_URL)

    expect(page.get_by_text('Strawberry')).to_be_visible()


def request_handler_two(route):
    response = route.fetch()
    response_list = response.json()

    my_fruit = {'name': 'Fruito-drillo', 'id': 912}

    response_list.append(my_fruit)

    route.fulfill(response=response, json=response_list)


def test_custom_and_original_fruits_are_visible_when_response_modified(page):
    page.route(FRUITS_API, request_handler_two)
    page.goto(PAGE_URL)

    expect(page.get_by_text('Strawberry')).to_be_visible()
    expect(page.get_by_text('Fruito-drillo')).to_be_visible()


def request_handler_three(route):

    fruit_list = [{'name': 'fruity_loops', 'id': 999}, {'name': 'looty_fruits', 'id': 998}]

    route.fulfill(json=fruit_list)

def test_shows_only_mocked_fruits(page):
    page.route(FRUITS_API, request_handler_three)
    page.goto(PAGE_URL)

    expect(page.get_by_text('fruity_loops')).to_be_visible()
    expect(page.get_by_text('looty_fruits')).to_be_visible()
    expect(page.get_by_text('Strawberry')).not_to_be_visible()



def request_handler_four(route):
    response = route.fetch()
    response_list = response.json()

    response_list[0]['name'] = 'yabloko'

    route.fulfill(response=response, json=response_list)


def test_shows_renamed_first_fruit(page):
    page.route(FRUITS_API, request_handler_four)
    page.goto(PAGE_URL)

    expect(page.get_by_text('yabloko')).to_be_visible()



def test_shows_loading_on_network_error(page):
    page.route(FRUITS_API, lambda route: route.abort())
    page.goto(PAGE_URL)

    expect(page.get_by_text('Loading...')).to_be_visible()
