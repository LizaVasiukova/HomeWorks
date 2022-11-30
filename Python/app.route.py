from urllib import request

import app as app
from flask import Flask, request

app = Flask(__name__)

import json


#topic13
"""""
@app.route('/leticia/<text>')
def f2():
    return "The queen"

"""

@app.route('/sum')
def sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("nuber2"))
    q = args.get("thequeen")
    sum = number1 + number2

    d = {
        "n1": number1,
        "n2": number2,
        "sum": sum,
        "TheQueen": q

    }

    return d


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


