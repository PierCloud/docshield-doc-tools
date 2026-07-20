from fastapi.testclient import TestClient

from docshield_doc_tools.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "docshield-doc-tools"}


def test_list_operations() -> None:
    response = client.get("/operations")

    assert response.status_code == 200
    assert response.json() == {"operations": ["merge-pdf"]}


def test_rejects_unknown_operation() -> None:
    response = client.post(
        "/jobs",
        json={"operation": "unknown", "input_refs": [], "options": {}},
    )

    assert response.status_code == 400

