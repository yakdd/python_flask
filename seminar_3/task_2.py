# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.
# ------------------------------------------------------------------------
from flask import Flask, render_template
from seminar_3.models2 import db, Author, Book
import csv
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/library.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('DB is done')


@app.cli.command('fill-db')
def fill_db():
    path_authors = os.path.join(os.getcwd(), 'seminar_3', 'authors.csv')
    path_books = os.path.join(os.getcwd(), 'seminar_3', 'books.csv')

    with open(path_authors, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            new_author = Author(firstname=line[0], lastname=line[1])
            db.session.add(new_author)
        db.session.commit()

    with open(path_books, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            new_book = Book(
                title=line[0],
                year=int(line[1]),
                id_author=int(line[2]),
                count=int(line[3])
            )
            db.session.add(new_book)
        db.session.commit()

    print('DB is full')


@app.route('/')
def index():
    return render_template('3_2.html')


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/db/')
def show_db():
    books = Book.query.all()
    authors = Author.query.all()
    context = {
        'title': 'Task 3.2',
        'h3': 'Список книг в базе данных',
        'books': books,
        'authors': authors,
    }
    return render_template('library.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
