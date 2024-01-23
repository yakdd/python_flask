# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом,
# где будет выведено введенное число и его квадрат.
# -------------------------------------------------
from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Task 7',
        'message': 'Введите число',
    }
    return render_template('task7.html', **context)


@app.route('/square_nuber/', methods=['GET', 'POST'])
def square_nuber():
    if request.method == 'POST':
        number = int(request.form.get('num'))
        return render_template('result.html',
                               message=f'{number} в квадрате равно {number ** 2}')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
