from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.crud import (
    create_incident,
    list_incidents,
)

from backend.schemas import (
    IncidentCreate,
    Question,
)

from backend.schemas import InvestigationRequest

from backend.services.search import similar_incidents

from backend.services.commander import investigate

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/incidents")
def create(data: IncidentCreate):

    incident_id = create_incident(
        data.title,
        data.description,
        data.severity,
        data.status,
        data.service
    )

    return {"incident_id": incident_id}


@app.get("/incidents")
def incidents():
    return list_incidents()

from uuid import UUID

from backend.crud import (
    add_note,
    add_resolution,
    delete_incident,
    get_incident,
    get_notes,
    get_resolutions,
    update_status,
)
from backend.schemas import (
    IncidentStatusUpdate,
    NoteCreate,
    ResolutionCreate,
)

@app.get("/incidents/{incident_id}")
def incident(incident_id: UUID):

    return get_incident(incident_id)

@app.delete("/incidents/{incident_id}")
def delete(incident_id: UUID):

    delete_incident(incident_id)

    return {"status": "deleted"}

@app.put("/incidents/{incident_id}/status")
def update(
    incident_id: UUID,
    body: IncidentStatusUpdate
):

    update_status(
        incident_id,
        body.status
    )

    return {"status": "updated"}

@app.post("/notes")
def note(body: NoteCreate):

    add_note(
        body.incident_id,
        body.author,
        body.note
    )

    return {"status": "ok"}

@app.get("/notes/{incident_id}")
def notes(incident_id: UUID):

    return get_notes(incident_id)

@app.post("/resolutions")
def resolution(body: ResolutionCreate):

    add_resolution(
        body.incident_id,
        body.resolution,
        body.resolved_by
    )

    return {"status": "ok"}

@app.get("/resolutions/{incident_id}")
def resolutions(incident_id: UUID):

    return get_resolutions(incident_id)

from backend.api.ai import analyze_incident

@app.get("/ai/{incident_id}")
def ai_analysis(incident_id: UUID):

    incident = get_incident(incident_id)

    if incident is None:
        return {"error": "Incident not found"}

    return analyze_incident(
        incident["title"],
        incident["description"]
    )
    
@app.post("/commander/investigate")
def commander(request: InvestigationRequest):

    return investigate(request.question)

@app.post("/search")
def search(data: Question):

    return similar_incidents(data.question)

app.mount(
    "/",
    StaticFiles(
        directory="backend/static",
        html=True
    ),
    name="static"
)