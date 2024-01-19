# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.
# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.
from flask import Flask, render_template
import jackets_db

app = Flask(__name__)


@app.route('/')
@app.route('/main/')
@app.route('/home/')
@app.route('/index/')
@app.route('/wear-shop/')
def index():
    context = {
        'title': 'Главная страница',
        'img': '/static/images/istockphoto.jpg'
    }
    return render_template('base.html', **context)


@app.route('/catalog/')
def catalog():
    context = {
        'breadcrumbs': '/home/catalog/',
        'title': 'Каталог товаров',
    }
    return render_template('catalog.html', **context)


@app.route('/basket/')
def basket():
    context = {
        'breadcrumbs': '/home/basket/',
        'title': 'Корзина товаров',
    }
    return render_template('basket.html', **context)


@app.route('/cloth/')
def cloth():
    context = {
        'breadcrumbs': '/home/catalog/cloth/',
        'title': 'Верхняя одежда',
    }
    return render_template('cloth.html', **context)


@app.route('/shoes/')
def shoes():
    context = {
        'breadcrumbs': '/home/catalog/shoes/',
        'title': 'Обувь',
    }
    return render_template('shoes.html', **context)


@app.route('/jackets/')
def jackets():
    context = {
        'breadcrumbs': '/home/catalog/cloth/jackets/',
        'title': 'Куртки',
        'jackets': jackets_db.jackets,
    }
    return render_template('jackets.html', **context)


@app.route('/jacket/<int:num>/')
@app.route('/jacket/')
def jacket(num):
    context = {
        'breadcrumbs': '/home/catalog/cloth/jackets/jacket/',
        'title': 'Куртка',
        'jacket': jackets_db.jackets[num - 1],
    }
    return render_template('jacket.html', **context, )


@app.route('/delivery/')
def delivery():
    context = {
        'breadcrumbs': '/home/delivery/',
        'title': 'Доставка',
    }
    return render_template('delivery.html', **context)


@app.route('/payment/')
def payment():
    context = {
        'breadcrumbs': '/home/payment/',
        'title': 'Оплата',
    }
    return render_template('payment.html', **context)


@app.route('/contacts/')
def contacts():
    _contacts = {
        'phone': '322-223',
        'address': 'а/я № 001',
        'email': 'e@mail.com',
    }

    context = {
        'breadcrumbs': '/home/contacts/',
        'title': 'Контакты',
        'contact': _contacts,
    }
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
