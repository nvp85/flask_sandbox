from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    # let's temporarly mock a user object
    user = {'username': 'test_user'}
    return render_template('index.html', title='Home', user=user)