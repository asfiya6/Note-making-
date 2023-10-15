from flask import Blueprint, render_template, request, flash, jsonify # BLUEPRINT defines a bunch of roots and urls inside it
from flask_login import login_required, current_user # current_user - detects whether a user is logged in or not and gives all
# the information about the user
from .models import Note
from . import db
import json # It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the
# client, so it can be displayed on a web page, or vice versa)

views = Blueprint('views', __name__) 


@views.route('/', methods=['GET', 'POST']) #runs everything inside homepage 
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id) #adding new note
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user) # to check if it is authenticated


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note: # to check if the note exists
        if note.user_id == current_user.id: # to cross check whether the notes are created by the particular user
            db.session.delete(note)
            db.session.commit()

    return jsonify({}) 