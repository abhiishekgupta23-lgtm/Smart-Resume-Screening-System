from pydantic import BaseModel


class ResumeRequest(BaseModel):
    job_description: str
    resume_text: str