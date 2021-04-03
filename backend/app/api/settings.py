from starlette.config import Config
from starlette.datastructures import Secret
from typing import List

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

CODE_BASE_ENV : str = config("CODE_BASE_ENV")

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

JWT_HASH_ALGORITHM :str = config("JWT_HASH_ALGORITHM")

ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", default="*",)

VERSION = "0.0.0"