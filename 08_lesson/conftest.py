import pytest
from api_client.project_client import ProjectClient


@pytest.fixture(scope="module")
def project_client():
    """
    Фикстура возвращает экземпляр API-клиента
    """
    return ProjectClient()
