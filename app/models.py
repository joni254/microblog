from datetime import datetime
<<<<<<< HEAD
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index= True, unique= True)
    email = db.Column(db.String(128), index = True, unique = True)
=======
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(50))
>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
<<<<<<< HEAD
        return 'User is {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(128), index = True, unique = True)
=======
        return 'user ni {}'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
<<<<<<< HEAD
        return 'Post is {}'.format(self.body)
=======
        return 'The post is {}'.format(self.body)
>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
