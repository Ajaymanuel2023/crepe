from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Create database engine with fallback
try:
    engine = create_engine(
        settings.DATABASE_URL,
        echo=True,  # Set to False in production
        connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
    )
except Exception as e:
    print(f"Database connection error: {e}")
    # Fallback to SQLite
    engine = create_engine(
        "sqlite:///./crepe.db",
        echo=True,
        connect_args={"check_same_thread": False}
    )

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()