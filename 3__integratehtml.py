""" Integrate html with flask code. It's just a jinja 2 template """


""" Dynamic url change or Building URL Dynamically!"""

# In order to display the some other pages we need ⬇️

# In order to read the posted values we need ⬇️


from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def welcome():
    # you need to have the folder structure like templates/index.html
    return render_template("index.html")


@app.route('/sucess/<int:score>')
def sucess(score):
    """ To run this : {http://127.0.0.1:5000/sucess/23}"""
    return render_template("result.html", result=score)


@app.route('/fail/<int:score>')
def fail(score):
    return f'You are fail because you score is 😭 {str(score)}'


@app.route(rule='/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        total_score = (science + maths) / 2

    if total_score >= 50:
        res = 'sucess'
    else:
        res = 'fail'

    return redirect(url_for(res, total_score))


@app.route('/results/<int:score>')
def results(score):
    if score < 50:
        res = 'fail'
    else:
        res = 'sucess'

    return redirect(url_for('sucess', score=score))


if __name__ == '__main__':
    app.run(debug=True)
