from core.api_client import BaseApiClient

class UserApiClient(BaseApiClient):
    def get_user_by_id(self, user_id):
        return self.get(f'/users/{user_id}')