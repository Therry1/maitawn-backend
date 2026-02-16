import os
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

# Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_DATABASE", "mon_api_db")
DB_USER = os.getenv("DB_USERNAME", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Engine
engine = create_async_engine(
    DATABASE_URL,
    echo=os.getenv("APP_DEBUG", "false").lower() == "true",
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Base pour les modèles
Base = declarative_base()


class Database:
    """Classe utilitaire pour gérer la base de données"""
    
    @staticmethod
    async def init_database():
        """Initialiser la connexion à la base de données"""
        async with engine.begin() as conn:
            # Créer les tables (en développement uniquement)
            if os.getenv("APP_ENV") == "development":
                await conn.run_sync(Base.metadata.create_all)
    
    @staticmethod
    def get_session_writer():
        """Retourne une session factory pour les opérations d'écriture"""
        return AsyncSessionLocal
    
    @staticmethod
    def get_session_reader():
        """Retourne une session factory pour les opérations de lecture"""
        return AsyncSessionLocal


# Dependency pour FastAPI
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency pour obtenir une session de base de données"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

