# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.
# ---------------------------------------------------------
from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Task 5',
        'message': 'Введите два числа и действие',
    }
    return render_template('task5.html', **context)


@app.route('/calculate/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        x = int(request.form.get('x'))
        y = int(request.form.get('y'))
        operator = request.form.get('operator')

        parameter = {
            '+': x + y,
            '-': x - y,
            '*': x * y,
        }
        result = parameter.get(operator)

        if operator == '/':
            try:
                result = str(x / y)
            except ZeroDivisionError:
                return render_template('error.html', message='Не надо делить на ноль!')

        return render_template('result.html', message=f'{x} {operator} {y} = {result}')


if __name__ == '__main__':
    app.run(debug=True)
