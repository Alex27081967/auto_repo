# 08_lesson/api_client/project_client.py

import requests

from config import BASE_URL, HEADERS


class ProjectClient:
    """
    Клиент для работы с методами API /projects
    """

    def __init__(self):
        self.base_url = f"{BASE_URL}/api-v2/projects"

    def create_project(self, name):
        """
        Создание проекта (POST /projects)
        """
        return requests.post(self.base_url, headers=HEADERS, json={"title": name})

    def get_project(self, project_id):
        """
        Получение проекта по ID (GET /projects/{id})
        """
        return requests.get(f"{self.base_url}/{project_id}", headers=HEADERS)

    def update_project(self, project_id, new_name):
        """
        Обновление названия проекта (PUT /projects/{id})
        """
        return requests.put(
            f"{self.base_url}/{project_id}", headers=HEADERS, json={"title": new_name}
        )
