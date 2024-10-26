from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models import db, User, DiaryEntry, PositiveNote
from flask_login import logout_user
from sqlalchemy.sql.expression import func
import random
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

import os

# Explicitly set the template folder path
template_dir = os.path.abspath("templates")
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key'

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates tables if they don't exist
    app.run(host="0.0.0.0", port=5000, debug=True)




# Home route
@app.route('/')
def home():
    return redirect(url_for('login'))




@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))  # Redirect to login page after logout


@app.route('/my_diary')
@login_required
def my_diary():
    entries = DiaryEntry.query.filter_by(user_id=current_user.id).all()
    return render_template('my_diary.html', entries=entries)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
        else:
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('diary'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html')

# Diary route
@app.route('/diary', methods=['GET', 'POST'])
@login_required
def diary():
    if request.method == 'POST':
        content = request.form['content']
        entry = DiaryEntry(content=content, user_id=current_user.id)
        db.session.add(entry)
        db.session.commit()
        flash('Diary entry added', 'success')
    entries = DiaryEntry.query.filter_by(user_id=current_user.id).all()
    return render_template('dairy.html', entries=entries)

#



import random

# Hard-coded notes
emotion_notes = {
    "happy": [
        "Keep pushing forward, you're doing amazing!",
        "Every day is a new opportunity to grow.",
        "Believe in yourself, you've got this!",
        "Smile and enjoy the little things.",
        "Focus on the positive moments.",
        "You're stronger than you think.",
        "Embrace the journey with a smile.",
        "Cherish each moment, no matter how small.",
        "Happiness is a journey, not a destination.",
        "Positive thoughts bring positive things."
    ],
    "sad": [
        "It’s okay to feel down; take things slow.",
        "Every struggle you face builds resilience.",
        "Take time to process your feelings.",
        "Crying is a strength, not a weakness.",
        "Healing takes time; be patient with yourself.",
        "This too shall pass; brighter days are coming.",
        "Remember, you’re not alone.",
        "Every storm will eventually clear.",
        "Give yourself permission to rest and recover.",
        "Let yourself heal one day at a time."
    ],
    "anxious": [
        "Breathe deeply; you’re doing your best.",
        "One day at a time; progress over perfection.",
        "You are capable of overcoming this challenge.",
        "Focus on what you can control.",
        "Keep pushing forward despite the fear.",
        "Anxiety doesn’t define your worth.",
        "Take small steps and celebrate each one.",
        "Believe in your resilience.",
        "Stay in the present moment; let go of worries.",
        "Focus on your breathing; stay grounded."
    ],
    "depressed": [
        "You are valued; this pain will pass.",
        "Hope is around the corner, even when it feels far.",
        "Reach out; there’s always someone who cares.",
        "You are stronger than the thoughts trying to bring you down.",
        "Your story is important and worth telling.",
        "Find light in the small things.",
        "Your struggles don’t define you.",
        "Give yourself grace and time.",
        "Be proud of your survival; you’re a warrior.",
        "You have overcome so much; keep going."
    ],
    "angry": [
        "Channel your energy in positive ways.",
        "Take a deep breath before reacting.",
        "Give yourself space to calm down.",
        "Focus your energy on finding solutions.",
        "Choose peace over conflict whenever possible.",
        "Redirect your anger into productive actions.",
        "Count to ten and breathe slowly.",
        "Forgiveness is for your own peace.",
        "Think before you act; respond with intention.",
        "Remember, not every battle is worth fighting."
    ]
}

@app.route('/jar')
@login_required
def jar():
    # Get the emotion from the query string if provided
    emotion = request.args.get('emotion')
    print(f"Emotion received: {emotion}")  # Debugging output

    # Retrieve a random note based on the specified emotion from the hardcoded dictionary
    if emotion in emotion_notes:
        note_content = random.choice(emotion_notes[emotion])
    else:
        note_content = ""  # Fallback message

    # Render template with the selected note
    return render_template('jar.html', note=note_content)


