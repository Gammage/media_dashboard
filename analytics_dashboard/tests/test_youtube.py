#import the modules to test the json data
#TODO reformat tests for fixtures, seperate files: one for youtube, one for instagram/tiktok, then a test file that references all 3 (Eventually) code getting too big brev
import pytest
from src.models.events_metrics import Eventid, Metric 

from pathlib import Path
import json


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
def metric_yt(youtube_json, youtube_snapshot):
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

def test_events_metrics(youtube_snapshot, metric_yt):

    assert isinstance(youtube_snapshot.metric_yt, dict) #check its a dictionary
    assert len(youtube_snapshot.metric_yt) > 0 #check if 0 metric_yts. we got to have at least one.
    for key, value in vars(metric_yt).items():
        if key != "event" and value is not None: #we want to make sure not to test the event attribute for metric_yts - it is part of the bidirectional link to EventId
            assert key in youtube_snapshot.metric_yt 
            assert youtube_snapshot.metric_yt[key] == value

    #test the bidirectional link from metric_yt to event
    assert metric_yt.event == youtube_snapshot

    
    # PYTHONPATH=. pytest


#analytics_dashboard/tests/tests_Events.py
#analyitcs_dashboard/main.py
# i cant seem toimport main in tests_events.py

#i have tried __init__.py to modulise
#i have tried .main, main


