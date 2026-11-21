from fastapi import FastAPI
from hooks.lifespan import lifespan
from hooks.middlewares import log_middleware
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI(title='user_api', lifespan=lifespan)

app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)


@app.get('/')
def root():
    logger.info('loguru生成的日志')
    return {'message': 'user_api is running'}


@app.get('/health')
def health():
    return {'status': 'ok'}
