from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "postgres"

#ЮРЛ Базы Данных
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#Ассинхронная версия движка алхимии
engine = create_async_engine(DATABASE_URL)

#Генератор сессии. Сессия - транзакция(набор инструкций) в БД
async_session_maker = sessionmaker(expire_on_commit=False, class_=AsyncSession, engine=engine)

#Класс используется для миграции БД, здесь аккумулируются метаданные,
#т.е. все данные всех классов БД
class Base(DeclarativeBase):
    pass