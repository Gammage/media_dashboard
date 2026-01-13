
# Media Dashboard (WIP)

If you joined here from !project on twitch, heres the complete breakdown of what im building

- see stream event log for updates so you can keep updated with whats going on!
- See WHAT AM I MAKING for entire scope of not only this project, but future ones I will stream. its all connected.

📺 I stream this project on twitch. see below for where im at;
🚨 Do not give me answers on stream! I will ask if at all, as I am still learning.
    - If I am doing something wrong, that is part of learning.

## Stream event log

### Typedict awareness, fixture scope 13/01/2026
    - I need to verify the dictionary is correct. didnt think about that, I just thought about testing it can be stored as an object or dictionary only. quackers told me about the typedict module
    - given how fixtures work, and their potential length/complexity, seperating them as fixtures is a good test standard. seperated fixtures from the tests
### Further refactoring, creating a dynamic metric attribute for eventid 12/01/2026
    - I have realised the need for metric to be both an object and a dictionary for eventid. maybe I need to store it as a simple dictionary? Maybe I need it as an object for greater analytics. by allowing both It enables scaleability.
    - seperated some of the tests in files

### Remembering Fixtures, Refactoring tests, modifying class scope 09/01/2026
    - this is a big one. so I had forgotten fixtures, which enables to store functions to be used across test functions. 
    - refactoring my test files to be DRY. That is, tests are assertions only. seperate test file for each api, then eventually a test file for all of them
    - So In the EventId, I was passing a paremeter for the metric attribute, then defining the actual attribute as an empty dictionary.
        - Even worse, my tests weren't using fixtures, so they passed. I then decided to keep the empty dictionary attribute for future project scope.
        - this still means an event can have a empty metric, with an attribute inside the metric class that enables a bidirectional link.

### Eventstore basics 07/01/2026
    - understanding how to create a class that will store multiple events (such as youtube video snapshots and their metrics)
    - creating a test that will make sure the logic of creating an object to store multiple events (and being able to test the class respective methods)

### event and metric class creation 05/01/2026
    - Learning the basics of class creation
    - how that would be used in an object to collect event data from a Youtube API
    - the youtube api is currently an example json file, with a nested dictionary for metrics
    - created a test to make sure the logic works. spent AGES understanding how to run the actual test and imports
    as they are a file outside of the src.

## WHAT AM I MAKING?

I am making a media dashboard that will serves mutiple purposes;
    - an analytics tool that will use an API to gather data from all social medias I use into one platform;
        - as part of the media analytics tool (im focusing on the analytics part first) it will also be a content scheduler for my YouTube, Instagram and TIKTOK(pending api limits)
    - to expand from this project, I will also build a fitness app and find means of downloading data from an Oura type product to track my health statistics. 
        - yet to determine if this will be one program or seperate. probably seperate.
    - to expand on this project scope, this will play a crucial part of my RAG setup for an LLM I will construct from scratch.


## Notes
This README will be updated as I build this live.
