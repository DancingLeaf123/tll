from pydantic import BaseModel


class ResultModel(BaseModel):
    code: int = 0
    message: str = "success"
    data: dict | None = None
