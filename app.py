from flask import Flask, request, jsonify, session, render_template
from src.Calculator import Calculator
from src.Util import Util

app = Flask(__name__)
app.secret_key = Util.generate_unique_key()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calculator')
def calculator():
    expr_args = request.args.get("expr")

    calc = Calculator()

    if '+' in expr_args:
        operands = expr_args.split('+')
        result = calc.calculateSum(int(operands[0]), int(operands[1]))
    elif '-' in expr_args:
        operands = expr_args.split('-')
        result = calc.calculateDiff(int(operands[0]), int(operands[1]))
    elif '*' in expr_args:
        operands = expr_args.split('*')
        result = calc.calculateProduct(int(operands[0]), int(operands[1]))
    elif '/' in expr_args:
        operands = expr_args.split('/')
        result = calc.calculateDiv(int(operands[0]), int(operands[1]))

    response = {}

    if session.get('calc_response') is None:
        response['data'] = [result]
        session['calc_response'] = response
    else:
        response = session.get('calc_response')
        result_list = response.get('data')
        result_list.insert(0, result)
        if len(result_list) > 10:
            result_list.pop()
        response['data'] = result_list
        session['calc_response'] = response

    return jsonify(response)


if __name__ == "__main__":
    app.run()
