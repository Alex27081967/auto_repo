import uuid


def test_create_project_positive(project_client):
    """
    Позитивный тест на создание проекта.
    Проверяет, что:
    - проект успешно создаётся (201)
    - возвращается id проекта
    - имя проекта корректно сохраняется (через GET-запрос)
    """
    name = f"Test Project {uuid.uuid4()}"
    response = project_client.create_project(name)
    assert response.status_code == 201

    response_json = response.json()
    print("\U0001f4e6 Ответ при создании проекта:", response_json)

    assert "id" in response_json
    project_id = response_json["id"]

    # Проверка, что проект действительно создан с нужным именем
    get_response = project_client.get_project(project_id)
    assert get_response.status_code == 200

    get_json = get_response.json()
    actual_name = get_json.get("title") or get_json.get("name")

    assert (
            actual_name is not None
    ), "Ответ от GET-запроса не содержит 'title' или 'name'"
    assert actual_name == name


def test_create_project_negative(project_client):
    """
    Негативный тест: попытка создать проект с пустым названием.
    Ожидается ошибка 400 или 422.
    """
    response = project_client.create_project("")
    assert response.status_code in [400, 422]


def test_get_project_positive(project_client):
    """
    Позитивный тест на получение проекта:
    - создаёт проект
    - получает его по ID
    - сравнивает имя
    """
    name = f"Read Test {uuid.uuid4()}"
    created = project_client.create_project(name).json()
    project_id = created["id"]

    response = project_client.get_project(project_id)
    assert response.status_code == 200

    actual_name = response.json().get("title") or response.json().get("name")
    assert actual_name == name


def test_get_project_negative(project_client):
    """
    Негативный тест: получение проекта по несуществующему ID.
    Ожидается ошибка 400 или 404.
    """
    response = project_client.get_project("invalid-id")
    assert response.status_code in [400, 404]


def test_update_project_positive(project_client):
    """
    Позитивный тест на обновление проекта:
    - создаёт проект
    - обновляет его имя
    - проверяет, что имя изменено
    """
    name = f"Update Test {uuid.uuid4()}"
    created = project_client.create_project(name).json()
    project_id = created["id"]

    new_name = f"Updated Name {uuid.uuid4()}"
    response = project_client.update_project(project_id, new_name)
    assert response.status_code == 200

    get_response = project_client.get_project(project_id)
    assert get_response.status_code == 200

    actual_name = get_response.json().get("title") or get_response.json().get("name")
    assert actual_name == new_name


def test_update_project_negative(project_client):
    """
    Негативный тест: попытка обновить несуществующий проект.
    Ожидается ошибка 400 или 404.
    """
    response = project_client.update_project("invalid-id", "Some name")
    assert response.status_code in [400, 404]
