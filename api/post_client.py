from core.api_client import BaseApiClient

class PostApiClient(BaseApiClient):
    def get_post_by_id(self, post_id: int):
        return self.get(f'/posts/{post_id}')

    def add_post(self, payload: dict, **kwargs):
        response = self.post('/posts', json=payload, **kwargs)
        return response

    def update_post(self, post_id: int, payload: dict, **kwargs):
        response = self.put(f'/posts/{post_id}', json=payload, **kwargs)
        return response

    def delete_post(self, post_id):
        response = self.delete(f'/posts/{post_id}')
        return response