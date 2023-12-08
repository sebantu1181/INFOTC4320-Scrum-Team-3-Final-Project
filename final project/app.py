from flask import Flask, render_template, flash, request, redirect, url_for, session 

app = Flask(__name__)

categories = ['Admin login', 'Reserve a set']
app.secret_key = 'infotec'

# admin usernames and passwords
users = {
    'admin1': {'password': '12345'},
    'admin2': {'password': '24680'},
    'admin3': {'password': '98765'},

}

# this will check to see if the passwords and usernames are valid
def admin_check(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method== 'POST':
        category = request.form['category']
        if category == 'Admin login':
            return redirect(url_for('admin'))
        elif category == 'Reserve a set':
            return redirect(url_for('reservation'))
        
    return render_template('index.html', catagories=categories)

# admin endpoint
@app.route('/admin', methods=['GET', 'POST'])
def admin():

    username = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if admin_check(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('admin'))  
        else:
            flash('Login not successful. Check username or password', 'danger')


    return render_template('admin.html', username=username)

@app.route('/reservations')
def reservation():
    return render_template('reservations.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
