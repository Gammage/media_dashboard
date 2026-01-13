import pytest
from src.models.events_metrics import Eventid, Metric 

from pathlib import Path
import json

# TODO need to define the dictionaries the json files will have. see typedict module

@pytest.fixture
def youtube_json():
    path = Path(__file__).resolve().parent.parent/"data"/"youtube_abc123_2026-01-01.json"
    content = path.read_text(encoding="utf-8")
    data = json.loads(content)
    return data


@pytest.fixture   
def youtube_snapshot(youtube_json):
    vid_snapshot = Eventid(
            platform=youtube_json.get("platform"),
            content_id=youtube_json.get("content_id"),
            timestamp=youtube_json.get("timestamp"),
        )

    return vid_snapshot


@pytest.fixture
def metric_obj(youtube_json, youtube_snapshot):
    #create the metric object
    #as metrics is nested in the json, we have to dig for these:
    metric_youtube_json = youtube_json.get("metrics",{}) #this calls upon that nested metrics dictionary. IMPORTANT

    #metrics later on references the items in this metric parameter(s)
    metric = Metric(
            views=metric_youtube_json.get("views"),
            likes=metric_youtube_json.get("likes"),
            subscribers=metric_youtube_json.get("subscribers"),
            comments=metric_youtube_json.get("comments"),
        )

    #add metric to event
    youtube_snapshot.metric_add(metric)
    return metric


