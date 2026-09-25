import os
import pytest
from api.post_client import PostApiClient
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def post_client():
    base_url = os.environ['BASE_URL']
    return PostApiClient(base_url)
