from flask import Flask, render_template, request, redirect, url_for, session
from database import *
from flask_wtf import FlaskForm
from wtforms import SelectField
import prompting as pr
import ytvideos as yt
import gtts  
import json

load_dotenv()

#DATABASE


app = Flask(__name__)
app.secret_key = os.urandom(12)
users = {}
@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password are valid (mock authentication)
        if username:
            response = checkUserExist(username)
            if response.count > 0 and response.items[0]["password"] == password:
            # Redirect to the add_numbers page after successful login
                session['username'] = username
                user = db.fetch({"username?contains": username}).items[0]
                session['qualification'] = user['qualification']
                session['learnertype'] = user['learnertype']

                return redirect(url_for('dashboard'))


        return 'Invalid credentials. Please try again.'

    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        dateofbirth =  request.form['date']
        qualification = request.form['qualification']
        learnertype = request.form['learnertype']

        # Check if username already exists (mock validation)
        if checkUserExist(username).count > 0:
            return 'Username already taken. Please choose another one.'
        try:
            user = insert_user(username, password, email, dateofbirth, qualification, learnertype)
        except Exception as e:
            
            print(f"Error: {str(e)}") 
        return f'Account created for {username}. You can now login.'

    return render_template('signup.html')
class MyForm(FlaskForm):
    mode = SelectField('Mode', choices=[('text', 'Text'), ('textarea', 'Textarea')])

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    # Check if the user is logged in
    result = None
    narration = None
    image_prompt = None
    if 'username' in session:
        username = session['username']
        if request.method == 'POST':
            mode = request.form.get('mode')
            subject = request.form.get('subject')
            value = request.form.get('value')
            print(mode)
            if mode == 'topic': 
                result = pr.responseOnTopic(value, subject)
            if mode == 'youtube':
                video_id = yt.getVideoID(value)
                print(video_id)
                print(type(video_id))
                transcript = yt.get_transcript(video_id)
                result = pr.responseOnVideo(transcript, subject)
                value = transcript
            learner = session['learnertype']
            print("learner: ", learner)
            """
            if learner == "auditory":
                narration = pr.generate_narration(value, result, subject)
                
                t1 = gtts.gTTS(narration)
                t1.save("audio.mp3")   
                main_file =  open("audio.mp3", "rb").read()
                dest_file = open('static/narration.mp3', 'wb+')
                dest_file.write(main_file)
                dest_file.close()
            if learner == "visual":
                image_prompt = pr.generatePrompt(value, subject=subject)
                pr.generateImage(image_prompt)"""

            



        session['result'] = result

        return render_template('dashboard.html', result = result, narration = narration, image_prompt = image_prompt)
    else:
        return redirect(url_for('signin'))
@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    # Your code to handle the quiz generation goes here
    # ...

    # Redirect to the quiz.html page after generating the quiz
    return redirect(url_for('quiz', response = session['result']))

@app.route('/quiz<response>', methods = ['GET', 'POST'])
def quiz(response):
    # Your code for the quiz.html page goes here
    # ...
    content = json.loads(pr.quizGenerator(response))

    print(content)
    return render_template('quiz.html', content = content)



if __name__ == '__main__':
    app.run(host='localhost', port=9874, debug=True)
