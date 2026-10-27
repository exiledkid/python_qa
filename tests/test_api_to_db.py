def test_post_from_api_is_saved_to_db(api_client, db_client):
    post_from_api = api_client.get_post_by_id(1).json()

    post_id = db_client.add_post(post_from_api['title'], post_from_api['body'])
    post_from_db = db_client.get_post_by_id(post_id)

    assert post_from_db[1] == post_from_api['title']
    assert post_from_db[2] == post_from_api['body']
