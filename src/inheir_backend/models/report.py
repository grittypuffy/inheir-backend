from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from ..config import AppConfig, get_config

config: AppConfig = get_config()

class Report(BaseModel):
    full_name: Optional[str] = None
    address: str
    email: Optional[EmailStr] = None
    report: str
    verdict: Literal["Pending", "Verified", "Not Verified"] = "Pending"
    reason: Optional[str] = None
    user_id: str = config.env.anonymous_user_id