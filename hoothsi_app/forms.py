from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Length

class InventoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    price = FloatField('Price', validators=[DataRequired()])
    mac_address = StringField('MAC Address', validators=[Length(max=20)])
    serial_number = StringField('Serial Number', validators=[Length(max=50)])
    manufacturer = StringField('Manufacturer', validators=[Length(max=50)])
    description = StringField('Description', validators=[Length(max=200)])
