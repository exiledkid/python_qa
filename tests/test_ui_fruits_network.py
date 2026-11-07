from playwright.sync_api import expect


SITE_URL = 'https://demo.playwright.dev/api-mocking/'

def test_fruits_api_returns_success_with_strawberry(page):

    with page.expect_response('**/api/v1/fruits') as response_info:
        page.goto(SITE_URL)

    response = response_info.value
    fruit_names = [fruit['name'] for fruit in response.json()]

    assert response.request.method == 'GET'
    assert response.status == 200
    assert 'Strawberry' in fruit_names


def test_all_fruits_from_api_are_shown_on_page(page):

    with page.expect_response('**/api/v1/fruits') as response_info:
        page.goto(SITE_URL)

    response = response_info.value
    fruit_names = [fruit['name'] for fruit in response.json()]


    for name in fruit_names:
        expect(page.get_by_text(name, exact=True)).to_be_visible()
