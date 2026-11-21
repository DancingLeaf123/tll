from fastapi import APIRouter

router = APIRouter(prefix='/address', tags=['地址'])


@router.get('/list')
async def get_address_list():
    return {'message': 'address list'}
