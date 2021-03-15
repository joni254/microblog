<<<<<<< HEAD
from app import app,db
=======
from app import app, db
>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
<<<<<<< HEAD
    return {'db': db, 'User': User, 'Post': Post}
=======
    return{'db':db, 'User': User, 'Post': Post}
>>>>>>> f45ac340741527f164a39a4937c29fdef26f15a4
