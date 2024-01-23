# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением,
# где будет выведено "Привет, {имя}!".
# ---------------------------------------
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'762bee78404dd9cfb79bc880789695865d840728a67bb66a79fec88e7f3dbf15'


@app.route('/')
def index():
    context = {
        'title': 'Task 8',
        'message': 'Введите Ваше имя',
    }
    return render_template('task8.html', **context)


@app.route('/name_flash/', methods=['GET', 'POST'])
def name_flash():
    if request.method == 'POST':
        user = request.form.get('name')
        if user:
            flash(f'Hello {user}', 'success')
            return redirect(url_for('name_flash'))
        flash('Введте имя', 'danger')
        return redirect(url_for('name_flash'))
    return render_template('flash.html')


if __name__ == '__main__':
    app.run(debug=True)
