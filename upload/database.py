import sqlalchemy

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = 'sqlite:///Sample.db'

engine = sqlalchemy.create_engine(DATABASE_URI, echo=False)

metadata = sqlalchemy.MetaData()
metadata.bind = engine

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()