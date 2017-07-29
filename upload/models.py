from database import Base
from sqlalchemy import Column, Integer, Sequence, String

class File(Base):
    __tablename__ = 'files'
    
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    name_readlabe =  Column(String(255), nullable=False)
    name =  Column(String(255), nullable=False, unique=True)