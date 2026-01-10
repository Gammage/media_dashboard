#import the modules to test the json data
#TODO reformat tests for fixtures, seperate files: one for youtube, one for instagram/tiktok, then a test file that references all 3 (Eventually) code getting too big brev
import pytest
from src.models.events_metrics import Eventid, Metric 

from pathlib import Path
import json

from src.models.eventstore import Event_store

@pytest.fixture
def youtube_json():
    path = Path(__file__).resolve().parent.parent/"data"/"youtube_abc123_2026-01-01.json"
    content = path.read_text(encoding="utf-8")
    data = json.loads(content)
    return data


@pytest.fixture
def instagram_json():
    path = Path(__file__).resolve().parent.parent/"data"/"instagram_abc123_2026-01-08.json"
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
def instagram_snapshot(instagram_json):
    vid_snapshot = Eventid(
            platform=instagram_json.get("platform"),
            content_id=instagram_json.get("content_id"),
            timestamp=instagram_json.get("timestamp"),
        )

    return vid_snapshot


@pytest.fixture
def metric_youtube_object(data_json, video_snapshot):
    #create the metric object
    #as metrics is nested in the json, we have to dig for these:
    metric_data_json = data_json.get("metrics",{}) #this calls upon that nested metrics dictionary. IMPORTANT

    #metrics later on references the items in this metric parameter(s)
    metric = Metric(
            views=metric_data_json.get("views"),
            likes=metric_data_json.get("likes"),
            subscribers=metric_data_json.get("subscribers"),
            comments=metric_data_json.get("comments"),
        )

    #add metric to event
    video_snapshot.metric_add(metric)
    return metric

@pytest.fixture
def event_store(video_snapshot, metric)



def test_events_metrics(video_snapshot, metric):

    assert isinstance(video_snapshot.metric, dict) #check its a dictionary
    assert len(video_snapshot.metric) > 0 #check if 0 metrics. we got to have at least one.
    for key, value in vars(metric).items():
        if key != "event" and value is not None: #we want to make sure not to test the event attribute for Metrics - it is part of the bidirectional link to EventId
            assert key in video_snapshot.metric 
            assert video_snapshot.metric[key] == value

    #test the bidirectional link from metric to event
    assert metric.event == video_snapshot

def test_eventstore():

    ## ASSERTIONS ##
    # .A. Empty store
    store = Event_store()
    assert store.all_events() == []
    
    # .B. single event
    store.event_add(event1)
    assert len(store.all_events()) == 1

    # .C. store all events
    store = Event_store()
    store.event_add(event1)
    store.event_add(event2)
    assert len(store.all_events()) == 2

    # .D. returning total views
    # TODO this test references the stored DICTIONARY not OBJECT. the event class holds an EMPTY DICTIONARY ATTRIBUTE so resets any metric parameter (for scaleability). remember
    assert store.total_views() == 300 

    # .E. calling the platform method which should return none (no event from tiktok) 
    events = store.platform_event("Tiktok")
    assert events == []

    # .F. test we can retrieve the platform type 
    youtube_event = store.platform_event("YouTube")
    for event in youtube_event:
        assert event.platform== "YouTube"

    
    # PYTHONPATH=. pytest


#analytics_dashboard/tests/tests_Events.py
#analyitcs_dashboard/main.py
# i cant seem toimport main in tests_events.py

#i have tried __init__.py to modulise
#i have tried .main, main


