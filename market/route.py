from market import app
from flask import render_template,redirect,url_for, flash
from market.models import Item, User
from market.forms import RegisterForm,Loginform
from market import db, bcrypt
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        password_hash =  bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=password_hash)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = Loginform()
    if form.validate_on_submit():
        
        attempted_user = User.query.filter_by(username=form.username.data).first()
        #print("password ==", attempted_user.password_hash)
        if attempted_user and attempted_user.check_password_correction(form.password.data):
        # if attempted_user and bcrypt.check_password_hash(attempted_user.password_hash, form.password.data):

            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)
    
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))