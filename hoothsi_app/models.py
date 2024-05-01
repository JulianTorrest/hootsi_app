from app import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    mac_address = db.Column(db.String(20))
    serial_number = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Inventory %r>' % self.name
