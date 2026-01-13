import pytest
from src.models.events_metrics import Eventid, Metric 

from pathlib import Path
import json

from src.models.eventstore import Event_store

@pytest.fixture
def instagram_json():
    path = Path(__file__).resolve().parent.parent/"data"/"instagram_abc123_2026-01-08.json"
    content = path.read_text(encoding="utf-8")
    data = json.loads(content)
    return data

@pytest.fixture   
def instagram_snapshot(instagram_json):
    vid_snapshot = Eventid(
            platform=instagram_json.get("platform"),
            content_id=instagram_json.get("content_id"),
            timestamp=instagram_json.get("timestamp"),
        )

    return vid_snapshot


