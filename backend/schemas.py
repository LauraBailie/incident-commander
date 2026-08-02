from uuid import UUID
from pydantic import BaseModel

class IncidentCreate(BaseModel):

    title:str
    description:str
    severity:str
    status:str
    service:str

class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: str
    status: str 
    service: str


class IncidentStatusUpdate(BaseModel):
    status: str


class NoteCreate(BaseModel):
    incident_id: UUID
    author: str
    note: str


class ResolutionCreate(BaseModel):
    incident_id: UUID
    resolution: str
    resolved_by: str
    
class InvestigationRequest(BaseModel):
    question: str
    
class Question(BaseModel):
    question:str