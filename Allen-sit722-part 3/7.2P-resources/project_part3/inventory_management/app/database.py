from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://allen_sit722_user:TWS2dg9t1BM0gxxHVHJYNCKmJZSlt2LD@dpg-cs1s16m8ii6s73d6u0e0-a.oregon-postgres.render.com/allen_sit722"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
 