# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено
# перенаправление на страницу ввода имени и электронной почты.
# ------------------------------------------------------------
from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Task 9',
        'message': 'Введите Ваше имя и E-mail',
    }

    if request.cookies.get('username'):
        logged = request.cookies.get('username')
        context['message'] = f'{logged}, Вы авторизованы!'

    return render_template('task9.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        context = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
        }
        response = make_response(render_template('task9_hello.html', user=context['name']))
        response.set_cookie('username', context['name'])
        response.set_cookie('useremail', context['email'])
        return response
    return redirect(url_for('index'))


@app.post('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', max_age=0)
    response.set_cookie('useremail', '', max_age=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
