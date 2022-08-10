from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user =User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')
    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address =email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists') 

    username = StringField(label='USERNAME', validators=[Length(min=2, max=30),DataRequired()])
    email_address= StringField(label ='EMAILADDRESS',validators=[Email(),DataRequired()])
    password1 = PasswordField(label ='ENTER PASSWORD', validators=[Length(min=5),DataRequired()])
    password2 = PasswordField(label ='CONFIRM PASSWORD', validators=[EqualTo('password1'),DataRequired()])
    submit= SubmitField(label ='CREATE ACCOUNT')


class Loginform(FlaskForm):
    username = StringField(label='USERNAME', validators=[DataRequired()])
    password = PasswordField(label ='PASSWORD', validators=[DataRequired()])
    submit= SubmitField(label ='SIGNIN')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')