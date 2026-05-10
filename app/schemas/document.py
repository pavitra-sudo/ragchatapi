from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):

    id: int

    filename: str

    created_at: datetime

    class Config:
        from_attributes = True