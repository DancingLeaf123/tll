from . import Base
from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy_serializer import SerializerMixin
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

class User(SerializerMixin, Base):
    __tablename__ = 'user'
    serialize_only = ('id', 'mobile', 'username', 'avatar',
                      'is_active', 'is_staff', 'last_login')
    serialize_rules = ('-password',)
    # 可空列序列化后会带 None，而 protobuf 的 string/bool 不接受 None，
    # 直接把 None 的字段从 dict 里剔掉，让 protobuf 用默认值
    exclude_values = (None,)
    id = Column(BigInteger, primary_key=True, default=generate_snowflake_id)
    mobile = Column(String(20), unique=True, index=True)
    username = Column(String(20), default=generate_username)
    password = Column(String(200), nullable=True)
    avatar = Column(String(200), nullable=True)
    is_active = Column(Boolean, nullable=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    last_login = Column(DateTime, nullable=True)
