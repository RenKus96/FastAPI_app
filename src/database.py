from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

import os


# SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://user_pg:user_pg@localhost:5432/appdb')

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user_pg:user_pg@localhost:5432/appdb"
#SQLALCHEMY_DATABASE_URL = "postgresql://user_pg:user_pg@db:5432/appdb"

engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()
