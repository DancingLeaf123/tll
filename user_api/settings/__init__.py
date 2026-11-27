from datetime import datetime, timedelta

JWT_SECRET_KEY = "yeahz_secret_key"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=2)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=15)

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

