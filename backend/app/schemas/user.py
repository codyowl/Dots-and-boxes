from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSerializer(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None

# serializers for user creation
class UserCreateSerializer(UserSerializer):
    email: EmailStr
    password: str

