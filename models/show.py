from models import db

class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    venue_name = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    artist_name = db.Column(db.String, nullable=False)
    artist_image_link = db.Column(db.String(500))
    start_time = db.Column(db.DateTime, nullable=False)