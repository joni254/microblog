from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'LOGIN', form = form)

@app.route('/', methods = ['POST'])


@app.route('/index', methods = ['GET'])
def index():
    user = {'username':'john'}
    posts = [
        {
            'author':{'username':'ndegwa'},
            'body':'Manchester won'
        },
        {
            'author':{'username':'Tilly'},
            'body':'Hot temperatures in ksm'
        }

    ]
    return render_template('index.html', title = 'HOME', user = user, posts = posts)