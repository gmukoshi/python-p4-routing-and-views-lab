#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = ""
    for i in range(parameter):
        numbers += f"{i}\n"
    return numbers


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 'Error: Invalid numbers provided!', 400

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero!'
        result = num1 / num2
        # ✅ Always return float string for division
        return str(result)
    elif operation == '%':
        if num2 == 0:
            return 'Error: Modulo by zero!'
        result = num1 % num2
    else:
        return f'Error: Operation "{operation}" not supported!'

    # 🧠 For all other ops, show integers cleanly if possible
    if result.is_integer():
        return str(int(result))
    else:
        return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
