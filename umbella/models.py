from datetime import datetime
from . import db



class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    slogan = db.Column(db.String(120), unique = True)
    description = db.Column(db.String(500), nullable = False)
    image = db.Column(db.String(60), nullable=False, default='Umbrella_black.png')
    umbrellas = db.relationship('Umbrella', backref = 'Series', cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Slogan: {}, Descrition: {}, Image: {} \n"
        str = str.format(self.id, self.name, self.slogan, self.description, self.image)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable = False),
    db.Column('umbrella_id', db.Integer, db.ForeignKey('umbrellas.id'), nullable = False),
    db.PrimaryKeyConstraint('order_id', 'umbrella_id'))

class Umbrella(db.Model):
    __tablename__ = 'umbrellas'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable=False)
    item_type = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable = False)
    color = db.Column(db.String(120), nullable=False)
    color_name = db.Column(db.String(120), nullable=False)
    pattern = db.Column(db.String(60), nullable=False)
    artist = db.Column(db.String, nullable = False)
    texture = db.Column(db.String(120), nullable = False)
    dimensions = db.Column(db.String(100), nullable = False)
    weight = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable = False)
    description_1 = db.Column(db.String(300), nullable=False)
    description_2 = db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    view = db.Column(db.String(60), nullable=False)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))


    def __repr__(self):
        str = "Id: {}, Model Name: {}, Item type: {}, Price: {}, Color: {}, Color Name: {}, Pattern: {}, Artist: {}, Texture: \"{}\", Dimension: {}, Weight: {}, Description: \"{}\",Description_1: \"{}\",Description_2: \"{}\", Image: {}, Series: {}, View:{} \n"
        str = str.format(self.id, self.name, self.item_type, self.price, self.color, self.color_name, self.pattern, self.artist,
                         self.texture, self.dimensions, self.weight, self.description, self.description_1, self.description_2, self.image, self.series, self.view)
        return str


class Order(db.Model):

    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime)
    umbrellas = db.relationship("Umbrella", secondary=orderdetails, backref="orders")
    totalcost = db.Column(db.Float)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    title = db.Column(db.String(32))
    postCode = db.Column(db.Integer)
    address = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    email = db.Column(db.String(128))
    

    def __repr__(self):
        str = "Id: {}, Status: {}, Date: {}, \nUmbrella: {}, Total Cost: {}, First Name: {}, Sur Name: {}, Title: {}, Postal Code: {}, Address: \"{}\", Phone: {}, Email: {}\n"
        str = str.format(self.id, self.status, self.date, self.umbrella, self.totalCost, self.firstName, self.surName,
                         self.title, self.postCode, self.address, self.phone, self.email)
        return str
