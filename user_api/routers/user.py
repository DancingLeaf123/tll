from fastapi import APIRouter
import string
import random

router = APIRouter(prefix='/user', tags=['用户'])


@router.get('/list')
async def get_user_list():
    return {'message': 'user list'}


@router.get('/smscode/{mobile}')
async def get_smscode():
    code = "".join(random.sample(string.digits, 4))
    return code