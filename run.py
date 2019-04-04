import os

from app import create_app, db
from app.models import Line
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Line=Line)


if __name__ == '__main__':
    app.run()
