from fastapi import FastAPI
from app.main.core.config import DEBUG, ALLOWED_HOSTS, VERSION
from starlette.middleware.cors import CORSMiddleware
from api.authentication import router

def get_application() -> FastAPI:
	application = FastAPI(debug=DEBUG, version=VERSION)

	application.add_middleware(
		CORSMiddleware,
		allow_origins=ALLOWED_HOSTS or ["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
		expose_headers=["Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"]
	)

	application.include_router(router)

	return application


app = get_application()