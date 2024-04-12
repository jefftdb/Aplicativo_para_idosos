from app import app,db
from flask import render_template,request,redirect,url_for
from model.login_model import User
from flask_login import login_user,logout_user


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods = ['GET' , 'POST'])
def register():
    if request.method == 'POST':   
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']
        
        if name and email and pwd:
            user = User(name,email,pwd)
            db.session.add(user)
            db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods = ['GET' , 'POST'])
def login():

    if request.method == 'POST':   

        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(debug=True)