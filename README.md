# 🚨 Incident Commander AI

An AI-powered incident management platform that helps Site Reliability Engineers investigate production incidents using semantic search and Amazon Bedrock.

---

## Features

- Create and manage production incidents
- AI-generated incident summaries
- Semantic search over historical incidents
- AI-powered incident investigation
- Root cause analysis
- Immediate remediation recommendations
- Long-term improvement suggestions
- REST API built with FastAPI
- Lightweight web dashboard

---

## Architecture

```
Frontend (HTML/CSS/JavaScript)
            │
            ▼
      FastAPI Backend
            │
    ┌───────┴────────┐
    ▼                ▼
CockroachDB     Amazon Bedrock
(Vector DB)     Claude + Titan
```

---

## Tech Stack

### Backend
- Python
- FastAPI
- Pydantic
- Psycopg3

### Database
- CockroachDB Cloud
- PostgreSQL
- pgvector (Distributed Vector Indexing)

### AI
- Amazon Bedrock
- Claude
- Titan Embeddings

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript

### Cloud & DevOps
- AWS
- CockroachDB ccloud CLI
- GitHub

---

## AI Workflow

1. User creates an incident.
2. Claude generates a concise incident summary.
3. Titan Embeddings converts the summary into a vector.
4. The vector is stored in CockroachDB.
5. During investigation, semantic search retrieves similar incidents.
6. Claude generates:
   - likely root cause
   - immediate actions
   - long-term recommendations
   - confidence score

---

## CockroachDB Features Used

### Distributed Vector Indexing

Historical incidents are stored as vector embeddings to enable semantic retrieval of similar incidents.

### ccloud CLI

Used to manage and inspect the CockroachDB Cloud deployment during development and testing.

---

## AWS Services Used

- Amazon Bedrock
  - Claude
  - Titan Embeddings

---

## Running Locally

Clone the repository.

```bash
git clone <repo-url>
cd incident-commander
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file containing:

```
DATABASE_URL=
AWS_REGION=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
BEDROCK_CHAT_MODEL=
BEDROCK_EMBEDDING_MODEL=
```

Run the application.

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## Future Improvements

- Slack integration
- CloudWatch alerts
- Multi-agent workflows
- Automatic incident timelines
- Authentication
- Grafana integration

---

## License

MIT