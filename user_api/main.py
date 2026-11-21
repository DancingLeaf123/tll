from fastapi import FastAPI

app = FastAPI(title='user_api')


@app.get('/')
def root():
    return {'message': 'user_api is running'}


@app.get('/health')
def health():
    return {'status': 'ok'}
