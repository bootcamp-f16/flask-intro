from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form, TextField, TextAreaField, validators, StringField, IntegerField, SubmitField

app = Flask(__name__, template_folder='templates')

class TimesForm(Form):
    x = IntegerField('x:', validators=[validators.required()])
    y = IntegerField('y:', validators=[validators.required()])

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/table', methods=['GET', 'POST'] )
def times():
    form = TimesForm(request.form)
    if request.method == 'POST':
        min = request.form['x'] or 1 
        max = request.form['y'] or 10 
    else:
        min = 1
        max = 10
    return render_template('table.html', min=int(min), max=int(max), form=form)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return render_template('post.html', post_id=post_id)
