#storing events.
#NOTE this file will be heavily changed when we get a db going. expect some placeholder stuff.

class Event_store:
    """storing the events and what we want from them"""

    def __init__(self):
        """storing the events"""
        self.events = []

    def event_add(self, event):
        """add an event"""
        self.events.append(event)

    def all_events(self):
        """list all events"""
        return self.events

    def platform_event(self, platform):
        """list platform of event (youtube etc)"""
        result = []
        for event in self.events:
            if event.platform == platform:
                result.append(event)
        return result

    def return_views(self):
        """list views"""

        views_list = []
        for event in self.events:
            views_list.append(event.metrics.views)
        return views_list
        #key: never return inside a loop if you want results from all iterations

    def total_views(self):
        """return total amount of views"""

        total = 0
        for event in self.events:
            total += event.metrics["views"] #verify referencing dict not object. metric is stored as dict in event
        return total
