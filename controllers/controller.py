
from flask import render_template, request
from markupsafe import re
from app import app
from models.event_list import add_new_event, events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title="Home", events=events)

@app.route('/events', methods=['POST'])
def add_event():
    print(request.form)
    event_title = request.form['name_of_event']
    event_date = request.form['date']
    event_guests = request.form['num_guests']
    event_room = request.form['room_location']
    event_description = request.form['description']
    new_event = Event(event_title, event_date, event_guests, event_room, event_description)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)

