def test_db_insert_and_read(db_client):

    test_body = 'Тело поста, тест'
    test_title = 'Заголовок, тест'

    post_id = db_client.add_post(test_title, test_body)

    post_from_db = db_client.get_post_by_id(post_id)
    
    assert post_from_db is not None
    assert post_from_db[1] == test_title
    assert post_from_db[2] == test_body


def test_db_delete_post(db_client):

    test_title = 'Заголовок тест 2'
    test_body = 'Тело поста тест 2'

    post_id = db_client.add_post(test_title, test_body)

    db_client.delete_post_by_id(post_id)

    post_that_doesnt_exist = db_client.get_post_by_id(post_id)

    assert post_that_doesnt_exist is None
    
    
def test_db_update_post(db_client):

    test_title = 'Тест заголовок 3'
    test_body = 'Тест тело 3'

    post_id = db_client.add_post(test_title, test_body)

    new_title = 'Заменённый заголовок 3'
    db_client.update_post_title(post_id, new_title)
    
    assert db_client.get_post_by_id(post_id)[1] == new_title


def test_db_insert_with_faker(faker, db_client):

    fake_title = faker.sentence()
    fake_body = faker.text()

    post_id = db_client.add_post(fake_title, fake_body)
    response = db_client.get_post_by_id(post_id)

    assert response is not None
    assert response[1] == fake_title
    assert response[2] == fake_body