import pytest
from fixtures.youtube_fixtures import youtube_json, youtube_snapshot, metric_yt

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



