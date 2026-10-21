from api.post import PostModel
from faker import Faker
import pytest

def test_get_post_contract(api_client):
    response = api_client.get_post_by_id(1)
    assert response.status_code == 200

    response_json = response.json()
    validated_response = PostModel(**response_json)
    assert validated_response.id == 1

def test_create_post(api_client, faker: Faker):
    title = faker.word()
    body = faker.sentence()
    userId = 1

    payload = {
        'title': title,
        'body': body,
        'userId': userId
    }

    response = api_client.add_post(payload)
    assert response.status_code == 201
    validated_response = PostModel(**response.json())
    assert validated_response.userId == userId
    assert validated_response.title == title
    assert validated_response.body == body

@pytest.mark.parametrize('post_id', [0, -1, 101, 'abc'],ids=['Id zero', 'Id negative number', 'Id above max', 'Id letters'])
def test_get_post_not_found(api_client, post_id):
    response = api_client.get_post_by_id(post_id)

    assert response.status_code == 404

@pytest.mark.xfail(reason='Test server accepts empty payload bug')
def test_create_post_empty_payload(api_client):
    payload = {}

    response = api_client.add_post(payload)

    assert response.status_code == 400