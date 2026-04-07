import os, time
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def wait_for_db(engine, max_retries=10, delay=2):
    for i in range(max_retries):
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("✅ Database is ready", flush=True)
            return
        except Exception:
            print(f"⏳ Database not ready, retrying... ({i+1}/{max_retries})", flush=True)
            time.sleep(delay)

    raise Exception("❌ Could not connect to the database")