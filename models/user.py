from . import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
import string
import random

def generate_username():
    # xxx123456
    code = "".join(random.sample(string.digits, 6))
    return '淘乐乐' + code

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    mobile = Column(String(20), unique=True, index=True)
    username = Column(String(20), default=generate_username)
    avatar = Column(String(200), nullable=True)
    is_active = Column(Boolean, nullable=True)
    is_staff = Column(Boolean, nullable=False)
    last_login = Column(DateTime, nullable=True)
