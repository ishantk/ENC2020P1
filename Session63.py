"""
FLASK         -> Framework to Create Light Weight Web Apps in Python | Django
PreRequisite  -> HTML and Python
Documentation -> https://flask.palletsprojects.com/en/1.1.x/
"""

from flask import Flask

# Creating a Python App running on Flask Server
app = Flask(__name__)

# Decorator -> @app.route()

# App Routing :) -> Routing the Outputs for different URLS

@app.route('/')
def welcome():
    message = "<html><body><center><h3>Welcome to Auribises</h3></center></body></html>"
    return message

@app.route('/home')
def home():
    message = "Search the Candle, Rather than Cursing the Darkness"
    return message

@app.route('/quote/<name>')
def quote(name):
    quote = "Dear, {} Work Hard, Get Luckier".format(name)
    return quote


if __name__ == '__main__':
    # app.run() # execute the app i.e. let the app run on Flask Server
    app.run(debug=True)     # Enable Debugging for the error