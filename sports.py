from flask import Flask,render_template,flash,redirect,session,logging,request,url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'admin@clinton'

# set up database
# app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db.sqlite3'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sports.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db  = SQLAlchemy(app)

# setting up classes
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(256),unique=True)



# homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    
    if request.method == 'POST' and form.validate():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        
        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash("You have successfully registered", "success")
        return redirect(url_for('/login'))
    
    else: 
        return render_template('register.html', form=form)

# login page
@app.route('/login/', methods=['GET', 'POST'])
def login(): 
    
    form = LoginForm(request.form) 
    if request.method == "POST" and form.validate():
        
        User = User.query.filter_by(email = form.email.data).first()
        
        if user:
            if check_password_hash(user.password, form.password.data):
                flash(message="You have successfully logged in", category="success")
            session['logged_in'] = True
            session['email'] = user.email
            session['username'] = user.username
            
            return redirect(url_for('/'))
        
        else:
            flash(message  = "email or password incorrect", category="danger")
            return render_template(url_for('/login.html'))
        
    return render_template('login.html', form=form)

# about page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# logout 
@app.route('/logout')
def logout():
    
    session['logged_in'] = False
    
    return redirect('url_for('/')')


if __name__ == '__main__':
    with app.app_context():
      db.create_all()
      app.run(debug=True)
    
    
    
    