from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)

categories = ['Admin login', 'Reserve a set']
app.secret_key = 'infotec'

# admin usernames and passwords
users = {
    'admin': {'password': '12345'},
    'admin2': {'password': '24680'},
    'admin3': {'password': '98765'},

}

# this will check to see if the passwords and usernames are valid
def admin_check(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html', catagories=categories)

# admin endpoint
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if admin_check(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')

    return render_template('admin.html')

@app.route('/reservations')
def reservation():
    return render_template('reservations.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
