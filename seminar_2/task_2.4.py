# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.
# -------------------------------------------------------------
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Task 4',
        'message': 'Введите текст',
    }
    return render_template('task4.html', **context)


@app.route('/word_count/', methods=['GET', 'POST'])
def word_count():
    if request.method == 'POST':
        input_text = request.form.get('text')
        count = len(input_text.split())
        return render_template('result.html', message=f'Количество слов: {count}')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
