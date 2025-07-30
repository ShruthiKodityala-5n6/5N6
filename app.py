from flask import Flask, request, render_template

app = Flask(__name__)  # Correct use of __name__

@app.route('/register', methods=['GET', 'POST']) 
def register():
    if request.method == 'POST': 
        name = request.form['name'] 
        email = request.form['email']
        password = request.form['password']
        # TODO: Save user data here (e.g., to a database or file)
        return render_template('success.html')  # POST success
    return render_template('register.html')  # Show form (GET)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
