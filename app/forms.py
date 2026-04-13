from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message='Title is required'),
        Length(max=255, message='Title must be less than 255 characters')
    ])
    description = TextAreaField('Description', validators=[
        DataRequired(message='Description is required')
    ])
    poster = FileField('Poster', validators=[
        FileRequired(message='Please select a poster image'),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only! (jpg, jpeg, png, gif)')
    ])