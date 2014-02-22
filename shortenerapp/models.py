from shortenerapp import db

class Url(db.Model):
    shortu = db.Column(db.String(10), primary_key=True)
    longu = db.Column(db.String(120))


