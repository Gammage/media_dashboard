import pytest
from src.models.events_metrics import Eventid, Metric 

from pathlib import Path
import json

from src.models.eventstore import Event_store


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


