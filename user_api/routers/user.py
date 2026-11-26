from fastapi import APIRouter
import string
import random
from schemas.result import ResultModel
from utils.cache import TLLRedis

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
    return ResultModel()