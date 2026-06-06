from flask import Flask, render_template_string, request, redirect, session
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey"

bcrypt = Bcrypt(app)

# Create Database
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')
conn.commit()
conn.close()

# Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                      (username, hashed_password))
            conn.commit()
            conn.close()
            return "Registration Successful!"
        except:
            return "Username already exists!"

    return '''
    <h2>Register</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
    '''

# Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[0], password):
            session['user'] = username
            return redirect('/dashboard')
        else:
            return "Invalid Credentials!"

    return '''
    <h2>Login</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    '''

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"<h2>Welcome {session['user']}</h2><br><a href='/logout'>Logout</a>"
    return redirect('/')

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)