<<<<<<< HEAD
from flask.helpers import url_for
from flask_login.utils import login_required, logout_user
from app.forms import LoginForm
from flask import render_template, flash, redirect, request
from app import app
from flask_login import current_user, login_user, logout_user
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect (next_page)
    return render_template('login.html', title = 'Sign In', form = form)
@app.route('/index')
@login_required
def index():
    user = {'username': 'John'}
    tweets = [{
        'author':{'username':'Amos'},
        'post':'Its a beautiful day'  
    },
    {
        'author':{'username':'Jane'},
        'post':'The boss just popped in'  
    }]
    return render_template('index.html', title = 'Home', user= user, tweets = tweets)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
=======
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
>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
