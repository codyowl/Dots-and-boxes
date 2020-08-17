from fastapi import APIRoute
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

router = APIRouter()

@router.post("/register",name="register")
async def register():
	pass

@router.post("/login",name="login")
async def login():
	pass	