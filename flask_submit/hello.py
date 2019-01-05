from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,RadioField,TextField
from wtforms.validators import DataRequired,Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

# flask 可以动态 更变页面，
# 可以动态生成form，按钮之间如何区分？
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    #sex = RadioField('abc')
    #certification = RadioField('certification', choices=['option1', 'option2'])
    #certification =RadioField('Label', choices=[('value', 'description'), ('value_two', 'whatever')])
class NameForm2(FlaskForm):
    name2 = StringField('name2?', validators=[DataRequired()])
    submit2 = SubmitField('Submit22')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    form2 = NameForm2()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = 'abc'
        print( form.submit)
    if form2.validate_on_submit():
        name = form2.name2.data
        form2.name2.data = 'abc2'
        print( form2.submit2)
    return render_template('index.html', form=form, name=name,form2=form2)
