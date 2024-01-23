# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.
# -------------------------------------------------------------
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Task 2',
    }
    return render_template('task2.html', **context)


@app.get('/download/')
def download_img_get():
    return render_template('download_img.html',
                           message='Загрузить файл')


@app.post('/download/')
def download_img_post():
    file = request.files.get('file')
    if file.filename:
        file_name = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(), 'static', 'images', file_name))
        return render_template('download_img.html',
                               message=f'Файл {file_name} загружен на сервер')
    return render_template('download_img.html',
                           message='Фал не выбран. Попробуйте еще раз!')


if __name__ == '__main__':
    app.run(debug=True)
