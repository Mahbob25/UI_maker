from pydantic import BaseModel, Field

class FileSchema(BaseModel):
    path: str = Field(..., description="File path including folders and extension")
    content: str = Field(..., description="Full source code of the file")
