# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
# -------------------------------------------------------------
from flask import Flask, render_template, request, url_for, redirect, jsonify
from seminar_3.models3 import db, User
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = b'102a35a7a7b22cc396889367d29aec3e6c572debe80b87442d75a02d0bf3be4c'
csrf = CSRFProtect(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/users.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('DB is done')


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/', methods=['GET', 'POST'])
def index():
    context = {
        'title': 'Task 3.8',
        'h3': 'Форма регистрации пользователя',
    }

    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        password = request.form.get('password')
        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        new_user = User(
            firstname=request.form.get('firstname'),
            lastname=request.form.get('lastname'),
            email=request.form.get('email'),
            password=password_hash
        )
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('3_8.html', **context, form=form)


@app.route('/db/')
def show_db():
    users = User.query.all()
    context = {
        'title': 'Task 3.8',
        'h3': 'Список пользователей',
        'users': users
    }
    return render_template('check.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
