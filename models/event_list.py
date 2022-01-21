from models.event import *

event1 = Event("Concert", "25/01/2022", 150, "Room 4", "Let's have a good time")
event2 = Event("Birthday Party", "15/02/2022", 8, "Room 2", "Spiderman's birthday")
events = [event1, event2]

def add_new_event(event):
    events.append(event)