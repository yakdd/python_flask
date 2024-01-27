# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
# ----------------------------------------------------------------------
from flask import Flask, render_template, request, url_for
from seminar_3.models import db, Student, Facultet, Gender
from string import ascii_letters as letters
from random import randint, choice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar3.db'  # cli
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/seminar3.db'    # route
db.init_app(app)


def name_generator():
    name = ''
    for i in range(randint(3, 15)):
        name += choice(letters)
    return name.title()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ok!')


@app.cli.command('fill-db')
def fill_db():
    faculties = ['Mathematics', 'Philosophy', 'Astronomy', 'IT']
    groups = ['101', '102', '201', '308', '404']

    for stream in faculties:
        new_facultet = Facultet(name_facultet=stream)
        db.session.add(new_facultet)
    db.session.commit()

    for i in range(20):
        new_gender = choice([Gender.male, Gender.female])
        new_student = Student(
            firstname=name_generator(),
            lastname=name_generator(),
            age=randint(17, 25),
            gender=new_gender,
            id_facultet=randint(1, len(faculties)),
            group=choice(groups)
        )
        db.session.add(new_student)
    db.session.commit()

    print('DataBase is full')


@app.route('/')
def index():
    return 'START!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/db/')
def db():
    students = Student.query.all()
    facultets = Facultet.query.all()
    context = {
        'students': students,
        'facultets': facultets,
        'h1': 'База данных студентов университета',
        'title': 'Task 3.1',
    }
    return render_template('3_1.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
