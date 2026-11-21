from contextlib import asynccontextmanager

from contextlib import asynccontextmanager
from fastapi import FastAPI
from loguru import logger




@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.add("logs/file.logs", rotation="500 MB", enqueue=True, level='INFO')
    yield
    # 程序即将结束之前，先把redis的连接关闭
