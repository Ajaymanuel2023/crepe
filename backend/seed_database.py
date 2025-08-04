from app.core.database import SessionLocal
from app.db.seed_data import create_seed_data

def main():
    db = SessionLocal()
    try:
        create_seed_data(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()