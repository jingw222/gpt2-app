from . import db


class Line(db.Model):
    __tablename__ = 'lines'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), unique=False)
    text = db.Column(db.String(64), unique=False)
    output = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return f'<Line {self.type!r} {self.id}>'
