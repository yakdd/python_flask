# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом
# или на страницу с ошибкой в случае некорректного возраста.
# -----------------------------------------------------------
from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Task 6',
        'message': 'Введите Ваше имя и возраст',
    }
    return render_template('task6.html', **context)


@app.route('/age-check/', methods=['GET', 'POST'])
def eighteen_plus():
    if request.method == 'POST':
        if request.form.get('age') >= str(18):
            return render_template('hello.html', user=request.form.get('name'))
        return render_template('error.html', message='Вам еще нет 18-ти лет!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
