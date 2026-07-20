# DocShield Doc Tools

Document tools microservice for the DocShield platform.

This service owns low-level document operations such as:

- merge PDF
- split PDF
- rotate PDF
- compress PDF
- PDF to images
- images to PDF

The service treats every input file as untrusted. Jobs should use isolated workspaces and short-lived files.

## Local Setup

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -e ".[dev]"
Copy-Item .env.example .env
.\.venv\Scripts\python.exe -m uvicorn docshield_doc_tools.main:app --reload --host 127.0.0.1 --port 8011
```

Open:

- API: http://localhost:8011
- Docs: http://localhost:8011/docs
- Health: http://localhost:8011/health

## Test

```powershell
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

## Current Operations

### `merge-pdf`

`POST /jobs`

```json
{
  "operation": "merge-pdf",
  "input_refs": [
    "C:/safe/workspace/a.pdf",
    "C:/safe/workspace/b.pdf"
  ],
  "options": {
    "output_ref": "C:/safe/workspace/merged.pdf"
  }
}
```

