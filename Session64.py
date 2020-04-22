"""
Flask:
    HTTP Requests
    File Uploading

For HTML : https://www.w3schools.com/html/

"""

from flask import *

# Creating a Python App running on Flask Server
app = Flask(__name__)

# Decorator -> @app.route()

# App Routing :) -> Routing the Outputs for different URLS

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

# @app.route('/login', methods=['GET', 'POST'])
@app.route('/login', methods=['POST'])
def validateLogin():
    email = request.form['txtEmail']
    password = request.form['txtPassword']

    # You can connect mysql or firebase firestore to validate the user from database
    if email == 'john@example.com' and password == 'pass123':
        # return "Welcome John"
        return redirect(url_for("home"))
    else:
        return "Invalid Credentials"

@app.route('/registeruser', methods=['POST'])
def registerUser():
    name = request.form['txtName']
    email = request.form['txtEmail']
    password = request.form['txtPassword']

    # You can connect mysql or firebase firestore to and save the details in the data base

    # return "{}, Thank You for Registering with us !!".format(name)
    return redirect(url_for("home"))

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/upload-data-set', methods=['POST'])
def uploadDataSet():
    if request.method == 'POST': # Just to Validate if user is uploading the file in POST Request
        file = request.files['dataset']
        file.save(file.filename)
        return render_template('success.html', name=file.filename)

@app.route('/upload-image', methods=['POST'])
def uploadImage():
    if request.method == 'POST': # Just to Validate if user is uploading the file in POST Request
        file = request.files['image']
        file.save(file.filename)
        return render_template('success.html', name=file.filename)

@app.route('/predict-label', methods=['GET', 'POST'])
def predictLabel():
    feature1 = request.form['feature1']
    feature2 = request.form['feature2']

    # ML/AI Algo goes here and do some predictions for the labels accordingly !!
    return "Setosa"

if __name__ == '__main__':
    # app.run() # execute the app i.e. let the app run on Flask Server
    app.run(debug=True)     # Enable Debugging for the error


# Explore Session Tracking: Cookies, URL Rewriting and the Built In Session Object in Flask :)