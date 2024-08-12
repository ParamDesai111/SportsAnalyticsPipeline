# webapp/backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database credentials
username = "SAPDBAdmin"
password = "sqladminParam!"
database = "SportsAnalyticsPipeline-DB"
server_name = "sportsanalyticspipeline-dbserver.database.windows.net"

# Construct the connection string
DATABASE_URL = f"mssql+pyodbc://{username}:{password}@{server_name}:1433/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
