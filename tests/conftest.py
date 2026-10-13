import pytest
from db.db_client import DbClient
from api.post_client import PostApiClient
from core.settings import Settings
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def pytest_addoption(parser):
    parser.addoption(
        '--env', 
        action='store', 
        default='dev', 
        help='Указывает окружение для запуска тестов (dev или stage)'
    )

@pytest.fixture
def settings(request):
    flag_name = request.config.getoption('--env')
    return Settings(_env_file=f'.env.{flag_name}')

@pytest.fixture
def api_client(settings):
    client = PostApiClient(settings.base_url)
    return client

@pytest.fixture
def db_client():
    db = DbClient()
    db.create_posts_table()
    return db

@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def products_page(page):
    return ProductsPage(page)
