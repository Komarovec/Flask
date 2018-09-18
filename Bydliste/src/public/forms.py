import re

from flask_wtf import Form
from wtforms.fields import BooleanField, TextField, PasswordField, DateTimeField, IntegerField,SelectField, DateField
from wtforms.validators import EqualTo, Email, InputRequired, Length

from ..data.models import User, LogUser
from ..fields import Predicate

def email_is_available(email):
    if not email:
        return True
    return not User.find_by_email(email)

def username_is_available(username):
    if not username:
        return True
    return not User.find_by_username(username)

def safe_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^[\w]+$', s) is not None

def postal_code(s):
    if not s:
        return True
    return re.match(r'^\d{3} \d{2}|\d{5}$',s) is not None

def house_number(s):
    if not s:
        return True
    return re.match(r'^[\d]+\/?[\d]+$',s) is not None

def name(s):
    if not s:
        return True
    return re.match(r'^[^\d]+$',s) is not None 


class LogUserForm(Form):

    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')

class secti(Form):
    hodnota1 = IntegerField("vlozHodnotu1", validators=[InputRequired(message="vyzadovano")])
    hodnota2 = IntegerField("vlozHodnotu2", validators=[InputRequired(message="vyzadovano")])
class masoform(Form):
    typ=SelectField('Typ', choices=[(1, "Hovezi"), (2, "Veprove")], default=2)

class UserForm(Form):
    street = TextField('Enter street:', validators=[
        Predicate(name, message="Please use only letters"),
        Length(min=2, max=50, message="Please use between 2 and 50 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    hNumber = TextField('Enter house number:', validators=[
        Predicate(house_number, message="Please use official format ex. 168/50"),
        Length(min=2, max=50, message="Please use between 2 and 50 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    city = TextField('Enter city', validators=[
        Predicate(name, message="Please use only letters"),
        Length(min=2, max=50, message="Please use between 2 and 50 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    postal = TextField('Enter postal code', validators=[
        Predicate(postal_code, message="Please keep CZ format ex. 747 70"),
        InputRequired(message="You can't leave this empty")
    ])

