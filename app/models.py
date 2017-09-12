from app import app, db

MAX_NAME_SIZE = 128
MAX_DESCRIPTION_SIZE = 2048

class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_SIZE), index=True, unique=True)
    description = db.Column(db.String(MAX_DESCRIPTION_SIZE), index=True, unique=True)

    def __repr__(self):
        return '%d:' % self.id + ' %s:' % self.name + ' %s' % self.description
