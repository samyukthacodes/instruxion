from flask import Flask, render_template, request, redirect, url_for, session
from database import *
from flask_wtf import FlaskForm
from wtforms import SelectField
import prompting as pr
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
                return redirect(url_for('dashboard'))


        return 'Invalid credentials. Please try again.'

    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists (mock validation)
        if checkUserExist(username).count > 0:
            return 'Username already taken. Please choose another one.'
        
        user = insert_user(username, password)

        return f'Account created for {username}. You can now login.'

    return render_template('signup.html')
class MyForm(FlaskForm):
    mode = SelectField('Mode', choices=[('text', 'Text'), ('textarea', 'Textarea')])

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    # Check if the user is logged in
    result = None
    if 'username' in session:
        username = session['username']
        if request.method == 'POST':
            mode = request.form['mode']
            subject = request.form['subject']
            prompt = request.form['prompt']
            result = pr.responseOnTopic(prompt, subject)
        return render_template('dashboard.html', result = result)
    else:
        return redirect(url_for('signin'))
    
    

if __name__ == '__main__':
    app.run(host='localhost', port=9874, debug=True)
