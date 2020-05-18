# import FlaskForm module from the Flask-wtf
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from wtforms.fields import StringField

# import valid state checking mechenisim
from wtforms.validators import InputRequired
from wtforms.validators import email


# form used in cart
class CheckoutForm(FlaskForm):
    firstname = StringField("Your first mame", validators=[InputRequired()])
    surname = StringField("Your Sur name", validators=[InputRequired()])
    title = StringField("Your title", validators=[InputRequired()])
    country = StringField("Your country", validators=[InputRequired()])
    postcode = StringField("zip code", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    phone = StringField("Your mobile", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    promotecode = StringField('promote code', validators=[InputRequired()])
    submit = SubmitField("Send to Agent")

