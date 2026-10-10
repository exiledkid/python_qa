from db.db_client import DbClient


def test_db_insert_and_read():
    db = DbClient()

    test_body = 'Тело поста, тест'
    test_title = 'Заголовок, тест'

    post_id = db.add_post(test_title, test_body)

    post_from_db = db.get_post_by_id(post_id)
    
    assert post_from_db != None
    assert post_from_db[1] == test_title
    assert post_from_db[2] == test_body


def test_db_delete_post():
    db = DbClient()
    
    test_title = 'Заголовок тест 2'
    test_body = 'Тело поста тест 2'

    post_id = db.add_post(test_title, test_body)

    db.delete_post_by_id(post_id)

    post_that_doesnt_exist = db.get_post_by_id(post_id)

    assert post_that_doesnt_exist == None
    
    
def test_db_update_post():
    db = DbClient()

    test_title = 'Тест заголовок 3'
    test_body = 'Тест тело 3'

    post_id = db.add_post(test_title, test_body)

    new_title = 'Заменённый заголовок 3'
    db.update_post_title(post_id, new_title)
    assert db.get_post_by_id(post_id)[1] == 'Заменённый заголовок 3'


def test_db_insert_with_faker(faker):
    db = DbClient()

    fake_title = faker.sentence()
    fake_body = faker.text()

    post_id = db.add_post(fake_title, fake_body)
    response = db.get_post_by_id(post_id)

    assert response != None
    assert response[1] == fake_title
    assert response[2] == fake_body