# Put your app in here.
from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

@app.route('/add')
def pipeitup():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)


@app.route('/sub')
def knockemdown():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)


@app.route('/mult')
def calculatedat():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)


@app.route('/div')
def breakitdown():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

methods = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<meth>')
def dodat(meth):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = methods[meth](a,b)

    return str(result)