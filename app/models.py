from app import db

class Callbacks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    phone = db.Column(db.Integer, index = True)
    ddi = db.Column(db.Integer, index = True)
    ticket = db.Column(db.Integer, index = True)
    platform = db.Column(db.String(64), index = True)
    created = db.Column(db.DateTime, index = True)
    cb_details = db.relationship('CallbackDetails', backref='comments', lazy='dynamic')

    def __repr__(self):
        return '<User %r' % (self.name)

class CallbackDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    updated = db.Column(db.DateTime)
    details = db.Column(db.String(64), index = True)
    private = db.Column(db.String(64), index = True)
    status = db.Column(db.String(64), index = True)
    callbacks_id = db.Column(db.Integer, db.ForeignKey('callbacks.id'))

    def __repr__(self):
        return '<User %r' % (self.id)
