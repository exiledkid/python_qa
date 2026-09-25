def test_add_post_success(post_client):
    payload = {
        'body': 'Тело поста',
        'title': 'Заголовок поста',
        'password': 'Секретный пароль'
    }
    response = post_client.add_post(payload=payload)
    assert response.status_code == 201
    resp_json = response.json()
    assert resp_json['body'] == 'Тело поста'

def test_get_post_by_id_success(post_client):
    response = post_client.get_post_by_id(1)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json['id'] == 1

def test_update_post_by_id_success(post_client):
    payload = {
        'password': 'secret_super_new_123'
    }

    response = post_client.update_post_by_id(1, json=payload)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json['password'] == 'secret_super_new_123'

def test_delete_post_by_id_success(post_client):
    response = post_client.delete_post_by_id(1)
    assert response.status_code == 200
    assert response.json() == {}

def test_get_post_by_id_fail(post_client):
        response = post_client.get_post_by_id(9999)
        assert response.status_code == 404