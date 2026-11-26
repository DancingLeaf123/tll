from fastapi import APIRouter, HTTPException
import string
import random
from utils.cache import TLLRedis
from schemas.response import ResultModel
from schemas.request import LoginModel
from google.protobuf.json_format import MessageToDict
import grpc
from protos import user_pb2, user_pb2_grpc

router = APIRouter(prefix='/user', tags=['用户'])

# 短信发送器延迟初始化：环境变量没配时不影响项目启动，
# 只有实际调用 /smscode 接口时才报错。
_sms_sender = None
tll_redis = TLLRedis()

def get_sms_sender():
    global _sms_sender
    if _sms_sender is None:
        _sms_sender = AliyunSMSSender()
    return _sms_sender


@router.get('/list')
async def get_user_list():
    return {'message': 'user list'}


@router.get('/smscode/{mobile}', response_model=ResultModel)
async def get_smscode(mobile: str):
    code = "".join(random.sample(string.digits, 4))
    # await (await get_sms_sender()).send_code(mobile, code)
    # await tll_redis.set(mobile, code)
    await tll_redis.set_sms_code(mobile, code)
    print('code:', code)
    return ResultModel(data={'code': code})

@router.post('/login')
async def login(data: LoginModel):
    mobile = data.mobile
    code = data.code
    cached_code = await tll_redis.get_sms_code(mobile)
    if code != cached_code:
        raise HTTPException(status_code=400, detail='验证码错误！')
    async with grpc.aio.insecure_channel('127.0.0.1:5001') as channel:
        stub = user_pb2_grpc.UserStub(channel)
        request = user_pb2.MobileRequest()
        request.mobile = mobile
        response = await stub.GetOrCreateUserByMobile(request)
        user = MessageToDict(response.user)
        return {
            'user': user,
            'access_token': 'access_token',
            'refresh_token': 'refresh_token'
        }