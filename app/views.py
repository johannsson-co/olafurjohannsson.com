from flask import render_template, flash, redirect, request, session, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html',
                          title='olafurjohannsson.com',
                          logged_in=session['logged_in'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = 'Invalid username'
        elif request.form['password'] != 'admin':
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/blog')
def blog():
    return render_template('blog.html')


