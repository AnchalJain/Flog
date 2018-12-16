from flask import render_template
from app import app
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