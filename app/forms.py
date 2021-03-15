from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
<<<<<<< HEAD
    submit = SubmitField('Sign In')
=======
    submit = SubmitField('Sign in')

>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
