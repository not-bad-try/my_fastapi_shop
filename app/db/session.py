from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Создание движка базы данных
engine = create_engine(settings.DATABASE_URL, echo=True)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()