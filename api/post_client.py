from core.client import BaseApiClient

class PostApiClient(BaseApiClient):
    def get_post_by_id(self, post_id):
        return self.get(f'/posts/{post_id}')

    def add_post(self, payload):
        return self.post('/posts/', json=payload)

    def update_post_by_id(self, post_id, **kwargs):
        return self.patch(f'/posts/{post_id}', **kwargs)

    def delete_post_by_id(self, post_id):
        return self.delete(f'/posts/{post_id}')