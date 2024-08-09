# webapp/backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mssql+pyodbc://<SAPDBAdmin>:<sqladminParam!>@<sportsanalyticspipeline-dbserver.database.windows.net>.database.windows.net:1433/<SportsAnalyticsPipeline-DB>?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
