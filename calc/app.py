# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask (__name__)

@app.route("/add")
def add_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = add(a,b)

    print(result)

    return f"{result}"

@app.route("/sub")
def sub_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = sub(a,b)

    return f"{result}"


@app.route("/mult")
def mult_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = mult(a,b)

    return f"{result}"


@app.route("/div")
def div_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = div(a,b)

    return f"{result}"


operations = {
    "add" : add, 
    "sub" : sub,
    "mult": mult,
    "div" : div,
}

@app.route("/math/<operation>")
def all_in_one(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = operations[operation](a, b)

    return f"{result}"
