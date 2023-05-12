from pydantic import BaseModel
from typing import Any, Optional
import ujson

class ResponseModel(BaseModel):
    status_code: int
    message: Optional[str] = None
    data: Optional[Any] = None
    
    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "message": "Success",
                "data": {"key": "value"}
            }
        }