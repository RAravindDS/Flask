""" Dynamic url change or Building URL Dynamically!"""

from flask import Flask

# To redirect to different page we need
from flask import redirect

# To build the url dynamically we need this ⬇️
from flask import url_for


app = Flask(__name__)


@app.route('/')
def welcome():
    return "This is my second Flask app!"


# Dynamic url by passing parameter to the route and this is called as variable rules!
@app.route('/sucess/<int:score>')  # providing parameter with type hints!
def sucess(score):
    """ To run this : {http://127.0.0.1:5000/sucess/23}"""
    return f'You passed the exam 🥳 {str(score)}'


@app.route('/fail/<int:score>')
def fail(score):
    return f'You are fail because you score is 😭 {str(score)}'


@app.route('/results/<int:score>')
def results(score):
    if score < 50:
        results = 'fail'
    else:
        results = 'sucess'

    # This will be directly redirected to this path!
    return redirect(url_for(results, score=score))  # url_for(url,values)


if __name__ == '__main__':
    app.run(debug=True)
