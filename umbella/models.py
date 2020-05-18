from datetime import datetime
from . import db

class Series():
    # db.Model

    # __tablename__ = 'series'
    # id = db.Column(db.Integer, primary_key = True)
    # name = db.Column(db.String(64), unique = True)
    # slogan = db.Column(db.String(120), unique = True)
    # description = db.Column(db.String(500), nullable = False)
    # image = db.Column(db.String(60), nullable=False, default='Umbrella_black.png')
    # umbrella = db.relationship('Umbrella', backref = 'Series', cascade="all, delete-orphan")

    def __init__(self, id, name, slogan, description, image):
        self.id = id
        self.name = name
        self.slogan = slogan
        self.description = description
        self.image = image

    def get_series_detail(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Slogan: {}, Descrition: {}, Image: {} \n"
        str = str.format(self.id, self.name, self.slogan, self.description, self.image)
        return str

# orderdetails = db.Table('orderdetails', 
# )


class Umbrella:


    def __init__(self, id, name, item_type, price, color, pattern, artist, texture, dimensions, weight, description, image, series, view):
        self.id = id
        self.name = name
        self.item_type = item_type
        self.price = price
        self.color = color
        self.pattern = pattern
        self.artist = artist
        self.texture = texture
        self.dimensions = dimensions
        self.weight = weight
        self.description = description
        self.image = image
        self.series = series
        self.view =view

    def get_umbrella_detail(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Model Name: {}, Item type: {}, Price: {}, Color: {}, Pattern: {}, Artist: {}, Texture: \"{}\", Dimension: {}, Weight: {}, Description: \"{}\", Image: {}, Series: {}, View:{} \n"
        str = str.format(self.id, self.name, self.item_type, self.price, self.color, self.pattern, self.artist,
                         self.texture, self.dimensions, self.weight, self.description, self.image, self.series, self.view)
        return str


class Order:
    def __init__(self, id, status, date, umbrella, message, totalCost, firstName, surName, title, country, postCode, address, phone, email, promoteCode):
        self.id = id
        self.status = status
        self.date = date
        self.umbrella = umbrella
        self.message = message
        self.totalCost = totalCost
        self.firstName = firstName
        self.surName = surName
        self.title = title
        self.country = country
        self.postCode = postCode
        self.address = address
        self.phone = phone
        self.email = email
        self.promoteCode = promoteCode

    def get_order_detail(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Status: {}, Date: {}, \nUmbrella: {}, Message: \"{}\", Total Cost: {}, First Name: {}, Sur Name: {}, Title: {}, Country: \"{}\", Postal Code: {}, Address: \"{}\", Phone: {}, Email: \"{}\", Promote Code: {} \n"
        str = str.format(self.id, self.status, self.date, self.umbrella, self.message, self.totalCost, self.firstName, self.surName,
                         self.title, self.country, self.postCode, self.address, self.phone, self.email, self.promoteCode)
        return str
