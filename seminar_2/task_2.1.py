# Создать страницу, на которой будет кнопка "Нажми меня",
# при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.
# -------------------------------------------------------
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Task 1',
        'username': 'MySuperUser'
    }
    return render_template('press_me.html', **context)


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return render_template('hello.html', user=request.form.get('username'))
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
