from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask_migrate import Migrate, migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
=======
from flask_migrate import Migrate
from flask_login import LoginManager





app = Flask(__name__)

#configs come here
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from app import routes, models
>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
