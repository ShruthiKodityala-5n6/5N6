from flask import Flask, request, render_template

app = Flask(__name__)  # Use __name__, not name

@app.route('/register', methods=['GET', 'POST']) 
def register():
    if request.method == 'POST': 
        name = request.form['name'] 
        email = request.form['email']
        password = request.form['password']
        # Here you would store the user data in a database or file
        return render_template('success.html')  # After processing POST
    return render_template('register.html')  # Show form for GET

if __name__ == '__main__':  # Use __name__ == '__main__'
    app.run(host='0.0.0.0', port=5000)  # Optional: specify port
