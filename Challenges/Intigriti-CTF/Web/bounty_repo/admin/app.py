from flask import Flask, Blueprint, request, jsonify, render_template, make_response, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'catsarethebest'
db = SQLAlchemy(app)


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


# Initialize the database
with app.app_context():
    db.create_all()
    # Add new users to the database
    admin_password_hash = generate_password_hash('sfd_234OSM@G9013qu-aCPU$8193')
    cat_password_hash = generate_password_hash('c4tz')
    admin = User(username='admin', password=admin_password_hash)
    cat = User(username='crypt0', password=cat_password_hash)
    db.session.add(admin)
    db.session.add(cat)
    db.session.commit()

# Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)


@app.route('/4dm1n_z0n3/')
def index():
    # Get the JWT token from the cookie
    access_token = request.cookies.get('auth')

    # Check if the user is logged in
    if access_token:
        return redirect('/4dm1n_z0n3/config')
    else:
        return render_template('login.html')


@auth_bp.route('/4dm1n_z0n3/login', methods=['POST'])
def login():
    # Implement user login and JWT generation logic here
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Include custom claims in the access token if needed
        access_token = jwt.encode({'identity': username}, app.config['JWT_SECRET_KEY'], algorithm='HS256')

        response = make_response(jsonify(message="Login successful"), 200)
        response.set_cookie('auth', value=access_token, max_age=3600, httponly=True)

        # Return the response, which will perform the redirection
        return response
    else:
        return jsonify(message='Invalid credentials'), 401


@auth_bp.route('/4dm1n_z0n3/config', methods=['GET'])
def config():
    # Get the JWT token from the cookie
    access_token = request.cookies.get('auth')

    # Check if the user is logged in
    if access_token:
        try:
            # Manually decode the JWT token
            token_data = jwt.decode(access_token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])

            # Retrieve the username (identity) from the decoded token
            username = token_data.get('identity')

            if username != 'admin':
                return render_template('config.html', username=username, config='only viewable by the admin')
            else:
                return render_template('config.html', username=username, config='INTIGRITI{w3b50ck37_5ql1_4nd_w34k_jw7}')
        except jwt.ExpiredSignatureError:
            return jsonify(message='Token has expired'), 401
        except jwt.InvalidTokenError:
            return jsonify(message='Invalid token'), 401
    else:
        return redirect('/4dm1n_z0n3')


@app.route('/4dm1n_z0n3/logout', methods=['POST'])
def logout():
    # Clear the authentication token (JWT) cookie
    response = redirect('/4dm1n_z0n3')
    response.delete_cookie('auth')
    return response


# Register the auth blueprint
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
