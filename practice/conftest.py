import pytest
from pydantic_settings import BaseSettings, SettingsConfigDict

def pytest_addoption(parser):
    parser.addoption('--stand', default='dev', help='Добавление возможности использования флага --stand')

class Settings(BaseSettings):
    city: str
    
    model_config = SettingsConfigDict(env_file='config.dev.txt', env_file_encoding='utf-8')



@pytest.fixture()
def settings(request):
    flag_name = request.config.getoption('--stand')
    file_name = f'config.{flag_name}.txt'

    return Settings(_env_file = file_name)