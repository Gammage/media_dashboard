import pytest
from src.models.events_metrics import Eventid, Metric 

from pathlib import Path
import json

from src.models.eventstore import Event_store

@pytest.fixture
def youtube_event():
    path = Path(__file__).resolve().parent.parent/"data"/"youtube_abc123_2026-01-01.json"
    content = path.read_text(encoding="utf-8")
    data = json.loads(content)


    vid_snapshot = Eventid(
            platform=data.get("platform"),
            content_id=data.get("content_id"),
            timestamp=data.get("timestamp"),
        )

    #storing the dictionary on youtube event as dictionary
    metric_data = data.get("metrics",{})
    

    #storing the metric dictionary on youtube event as an object
    metric = Metric(
            views=data.get("views"),
            likes=data.get("likes"),
            subscribers=data.get("subscribers"),
            comments=data.get("comments"),
        )

    #add metric to event
    youtube_snapshot.metric_add(metric)



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


