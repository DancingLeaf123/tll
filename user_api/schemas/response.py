from pydantic import BaseModel
from enum import Enum


class ResultEnum(Enum):
    SUCCESS = 1
    FAILURE = 2


class ResultModel(BaseModel):
    result: ResultEnum = ResultEnum.SUCCESS