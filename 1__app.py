""" This code is a basic skeletion of flask"""

# import the flask if you don't have flask "pip install flask"
from flask import Flask

# create a app name
# this is our WSGI application (it will help us to communicate with server)
app = Flask(__name__)


# this will take 2 parameter (rule : str(url of the web page), options)
@app.route('/')
def welcome():
    return "This is my First Flask APP: debug = True"


@app.route('/members')
def members():
    return "This is the members page!"


if __name__ == "__main__":
    app.run(debug=True)
    # we have four parameters inside the function run()
    # just run python 1__app.py
