from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.config import NON_DEV
from src.operations.router import get_specific_operations

router = APIRouter(
    prefix='',
    tags=['Pages'],
)

templates = Jinja2Templates(directory='src/templates')


@router.get('/')
def get_base_page(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})


@router.get("/search/{operation_type}")
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    return templates.TemplateResponse(
        "search.html",
        {"request": request, "operations": operations["data"]}
    )


@router.get('/chat')
def get_chat_page(request: Request):
    if bool(int(NON_DEV)):
        return templates.TemplateResponse('chat.html', {'request': request})
    else:
        return templates.TemplateResponse('chat_non_dev.html', {'request': request})
