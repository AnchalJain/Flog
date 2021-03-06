from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
#home view function
@app.route('/')
@app.route('/index')
def index():
    user={'username':'Anchal'}
    posts=[
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Poland'
        },
        {
            'author':{'username':'Aditya'},
            'body': 'Avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home',user=user,posts=posts)
    # here I am using render template function
#login view function
@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)
