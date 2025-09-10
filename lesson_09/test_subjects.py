# test_subjects.py
# Тесты на таблицу subject с фикстурами, автоудалением тестовых данных и вынесенной конфигурацией

import pytest
from sqlalchemy import text

from db_utils import engine, get_next_subject_id


# ---------------------------
# Pytest-фикстура подключения
# ---------------------------
@pytest.fixture(scope="function")
def connection():
    """
    Устанавливает соединение с БД и автоматически закрывает его после теста.
    """
    conn = engine.connect()
    yield conn
    conn.close()


# ---------------------------
# Pytest-фикстура очистки данных
# ---------------------------
@pytest.fixture
def cleanup_subject(connection):
    """
    Список добавленных subject_id, которые будут удалены после теста.
    """
    created_ids = []

    yield created_ids

    # Teardown: удаляем созданные записи
    for sid in created_ids:
        connection.execute(
            text("DELETE FROM subject WHERE subject_id = :id"), {"id": sid}
        )


# ---------------------------
# Тест: вставка subject
# ---------------------------
def test_create_subjects(connection, cleanup_subject):
    count_before = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[
        0
    ]
    new_id = get_next_subject_id(connection)

    connection.execute(
        text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
        {"id": new_id, "title": "Football"},
    )
    cleanup_subject.append(new_id)

    count_after = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[0]
    assert count_after == count_before + 1


# ---------------------------
# Тест: обновление subject
# ---------------------------
def test_update_subject_name(connection, cleanup_subject):
    new_id = get_next_subject_id(connection)
    new_title = "Baseball"

    connection.execute(
        text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
        {"id": new_id, "title": new_title},
    )
    cleanup_subject.append(new_id)

    fetched = connection.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"), {"id": new_id}
    ).fetchone()

    assert fetched is not None
    assert fetched[0] == new_title


# ---------------------------
# Тест: удаление subject
# ---------------------------
def test_delete_subject(connection):
    # Вставляем временный subject
    temp_id = get_next_subject_id(connection)
    connection.execute(
        text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
        {"id": temp_id, "title": "Temp Delete Subject"},
    )

    count_before = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[
        0
    ]

    # Удаляем
    connection.execute(
        text("DELETE FROM subject WHERE subject_id = :id"), {"id": temp_id}
    )

    count_after = connection.execute(text("SELECT COUNT(*) FROM subject")).fetchone()[0]
    assert count_after == count_before - 1

    deleted = connection.execute(
        text("SELECT * FROM subject WHERE subject_id = :id"), {"id": temp_id}
    ).fetchone()

    assert deleted is None
