import os
import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import role
from src.auth.schemas import RoleCreate
from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=['Operations']
)


@router.post('/post_role')
async def post_role(
        data: RoleCreate,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        stmt = insert(role).values(id=int(data.id), name=data.name, permissions=None)
        await session.execute(stmt)
        await session.commit()
        return {'status': 'success'}
    except Exception as exc:
        return {'status': exc}


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"


@router.get('/')
async def get_specific_operations(
        operation_type: str,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            'status': 'success',
            'data': result.mappings().all(),
            'details': None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': None
        })


@router.post('/')
async def add_specific_operations(
        new_operation: OperationCreate,
        session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}


@router.get("/main")
async def main(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(1))
    return result.mappings().all()
