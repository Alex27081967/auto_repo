# db_utils.py
# Создание подключения к базе данных и вспомогательные функции

from sqlalchemy import create_engine, text

from config import DB_CONFIG

# Формируем строку подключения
DB_URL = (
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# Создаём engine SQLAlchemy
engine = create_engine(DB_URL)


def get_next_subject_id(connection):
    """Возвращает следующий свободный subject_id"""
    max_id = connection.execute(text("SELECT MAX(subject_id) FROM subject")).fetchone()[
        0
    ]
    return (max_id or 0) + 1
