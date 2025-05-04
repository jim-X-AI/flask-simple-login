from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database
users = {
    1: {"username": "Alice", "password": "password123"},
    2: {"username": "Bob", "password": "password456"},
    3: {"username": "Charlie", "password": "password789"}
}

@app.route('/')
def index():
    return render_template('web_create.html', message="Welcome, Stranger!")

@app.route('/login', methods=['POST'])
def login():
    user_id = int(request.form['user_id'])
    password = request.form['password']
    
    user = users.get(user_id)
    
    if user and user['password'] == password:
        return render_template('web_create.html', username=user['username'])
    else:
        return render_template('web_create.html', message="Invalid ID or password. Please try again.")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

