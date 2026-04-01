from pydantic import BaseModel

class jobRequest(BaseModel):
    job_description: str