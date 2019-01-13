from flask_script import Manager
from flask_migrate import MigrateCommand

from wedding_gallery import app
from wedding_gallery.models import DBSession, db, core

manager = Manager(app)


@app.shell_context_processor
def make_shell_context():
    return {'DBSession': DBSession,
            'db': db,
            'core': core}


@manager.option('-h', '--host', dest='host', default='0.0.0.0')
@manager.option('-p', '--port', dest='port', type=int, default=5000)
def server(host, port):
    app.run(host=host, port=port, threaded=True)


if __name__ == '__main__':
    manager.add_command('db', MigrateCommand)
    manager.run()
