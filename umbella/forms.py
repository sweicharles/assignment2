# import FlaskForm module from the Flask-wtf
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField
from wtforms.fields import StringField
from wtforms.fields import SelectField

# import valid state checking mechenisim
from wtforms.validators import InputRequired
from wtforms.validators import email

# form used in cart
class CheckoutForm(FlaskForm):
    firstname = StringField("Your first mame", validators=[InputRequired()])
    surname = StringField("Your last name", validators=[InputRequired()])
    # limited the options by using select field
    title = SelectField('Your title',
                        choices=[('1', 'Mr.'), ('2', 'Ms.'), ('3', 'Mrs.'),
                                 ('4', 'Miss'), ('5', 'None')])
    postcode = StringField("zip code", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    phone = StringField("Your mobile", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    submit = SubmitField("Send to Agent")

