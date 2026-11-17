from . import Base
from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
import string
import random
from utils.snowflake.snowflake import Snowflake
from settings import DATACENTER_ID, WORKER_ID
snowflake = Snowflake(DATACENTER_ID, WORKER_ID)

def generate_username():
    # xxx123456
    code = "".join(random.sample(string.digits, 6))
    return '淘乐乐' + code

def generate_snowflake_id():
    new_id = snowflake.get_id()
    return new_id

class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True, default=generate_snowflake_id)
    mobile = Column(String(20), unique=True, index=True)
    username = Column(String(20), default=generate_username)
    avatar = Column(String(200), nullable=True)
    is_active = Column(Boolean, nullable=True)
    is_staff = Column(Boolean, nullable=False)
    last_login = Column(DateTime, nullable=True)
