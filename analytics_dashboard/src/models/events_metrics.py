from datetime import datetime

class Eventid:
    """define what happened"""

    def __init__(self, platform=None, content_id=None, timestamp=None):
        """define event attributes"""

        self.platform = platform
        self.content_id= content_id

        #self.metrics has to be a dictionary. think about how we reference this data. views(key) has a number(int or str idk yet)
        self.metrics = {} #a dictionary of metrics 
        self.timestamp = timestamp

    def metric_add(self, metric):
        """includes the metrics that come with the event"""
        metric.event = self # link back to this Eventid
        
        for key, value in vars(metric).items():
            if key != "event" and value is not None:
                self.metrics[key] = value


#metrics

class Metric:
    """define the metrics of the content"""

    def __init__(self, views=None, likes=None, subscribers=None, comments=None):
        """metrics of the content"""
        self.views = views
        self.likes = likes
        self.subscribers = subscribers
        self.comments = comments

        #Eventually when metrics wants to point back to Eventid;
        self.event = None # will point to the eventID instance


