from api.user import UserModel

def test_get_user(user_api_client):
    response = user_api_client.get_user_by_id(1)

    assert response.status_code == 200

    validated_response = UserModel(**response.json())

    assert validated_response.id == 1