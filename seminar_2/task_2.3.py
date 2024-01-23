# Создать страницу, на которой будет форма для ввода логина и пароля.
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля
# и переход на страницу приветствия пользователя или страницу с ошибкой.
# ---------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USER_DATA = {
    'login': 'admin',
    'password': 'qwerty',
}


@app.route('/')
def index():
    context = {
        'title': 'Task 3',
        'message': 'Введите логин и пароль',
    }
    return render_template('task3.html', **context)


@app.route('/autho/', methods=['GET', 'POST'])
def authorization():
    if request.method == 'POST':
        input_login = request.form.get('login')
        input_password = request.form.get('password')
        if (input_login == USER_DATA['login']) and (input_password == USER_DATA['password']):
            context = {
                'title': 'Hello user',
                'message': f'Hello, {input_login}!'
            }
            return render_template('task3_hello.html', **context)
        return render_template('error.html', message='Ошибка!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
