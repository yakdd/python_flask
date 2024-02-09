from fastapi import FastAPI
import databases
import sqlalchemy
from typing import List
from random import randint
from datetime import datetime
from homework_6.users_model import create_password, User, UserIn
from homework_6.goods_model import create_price, Goods, GoodsIn
from homework_6.orders_model import Order, OrderIn

DATABASE_URL = 'sqlite:///OnlineStore.db'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('firstname', sqlalchemy.String(32)),
    sqlalchemy.Column('lastname', sqlalchemy.String(64)),
    sqlalchemy.Column('email', sqlalchemy.String(128)),
    sqlalchemy.Column('password', sqlalchemy.String(32)),
)

goods_table = sqlalchemy.Table(  # gds
    'goods',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(32)),
    sqlalchemy.Column('description', sqlalchemy.String(500)),
    sqlalchemy.Column('price', sqlalchemy.Float),
)

orders_table = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey(users_table.columns.id)),
    sqlalchemy.Column('goods_id', sqlalchemy.ForeignKey(goods_table.columns.id)),
    sqlalchemy.Column('orderdate', sqlalchemy.DateTime()),
    sqlalchemy.Column('is_active', sqlalchemy.Boolean(), server_default=sqlalchemy.sql.expression.true()),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)
app = FastAPI()

default_users = 5  # кол-во фейковых пользователей
default_goods = 25  # кол-во фейковых товаров
default_orders = 10  # кол-во фейковых заказов


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/')
async def root():
    return {'message': 'Homework # 6'}


@app.get('/fake-db/')
async def fill_default_db():
    for i in range(default_users):
        query = users_table.insert().values(
            firstname=f'fake_Name_{i}',
            lastname=f'fake_Surname_{i + 1}',
            email=f'fake_email_{i + 1}@email.net',
            password=create_password())
        await database.execute(query)

    for i in range(default_goods):
        query = goods_table.insert().values(
            name=f'Product_{i + 1}',
            description=f'Product_description_{i + 1}',
            price=create_price())
        await database.execute(query)

    for i in range(default_orders):
        user_id = randint(1, default_users)
        gds_id = randint(1, default_goods)
        query = orders_table.insert().values(
            user_id=user_id,
            goods_id=gds_id,
            orderdate=datetime.now(), )
        await database.execute(query)

    return {
        'message': f'Default db created with {default_users} users, {default_goods} goods, {default_orders} orders.'}


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users_table.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users_table.select().where(users_table.c.id == user_id)
    return await database.fetch_one(query)


@app.get('/goods/', response_model=List[Goods])
async def read_goods():
    query = goods_table.select()
    return await database.fetch_all(query)


@app.get('/goods/{goods_id}', response_model=Goods)
async def read_gds(goods_id: int):
    query = goods_table.select().where(goods_table.c.id == goods_id)
    return await database.fetch_one(query)


@app.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders_table.select()
    return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id: int):
    query = orders_table.select().where(orders_table.c.id == order_id)
    return await database.fetch_one(query)


# Поиск заказов по пользователю:
@app.get('/orders-user/{user_id}', response_model=List[Order])
async def orders_by_user(user_id: int):
    query = orders_table.select().where(orders_table.c.user_id == user_id)
    return await database.fetch_all(query)


# Поиск заказов по товару:
@app.get('/orders-gds/{goods_id}', response_model=List[Order])
async def orders_by_gds(goods_id: int):
    query = orders_table.select().where(orders_table.c.goods_id == goods_id)
    return await database.fetch_all(query)


@app.post('/users/', response_model=User)
async def create_user(new_user: UserIn):
    query = users_table.insert().values(**new_user.dict())
    new_id = await database.execute(query)
    return {**new_user.dict(), 'id': new_id}


@app.post('/goods/', response_model=Goods)
async def create_gds(new_gds: GoodsIn):
    query = goods_table.insert().values(**new_gds.dict())
    new_id = await database.execute(query)
    return {**new_gds.dict(), 'id': new_id}


@app.post('/orders/', response_model=Order)
async def create_order(new_order: OrderIn):
    query = orders_table.insert().values(**new_order.dict())
    new_id = await database.execute(query)
    return {**new_order.dict(), 'id': new_id}


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, up_user: UserIn):
    query = users_table.update().where(users_table.c.id == user_id).values(**up_user.dict())
    await database.execute(query)
    return {**up_user.dict(), 'id': user_id}


@app.put('/goods/{goods_id}', response_model=Goods)
async def update_gds(goods_id: int, up_goods: GoodsIn):
    query = goods_table.update().where(goods_table.c.id == goods_id).values(**up_goods.dict())
    await database.execute(query)
    return {**up_goods.dict(), 'id': goods_id}


@app.put('/orders/{order_id}', response_model=Order)
async def update_order(order_id: int, up_order: OrderIn):
    query = orders_table.update().where(orders_table.c.id == order_id).values(**up_order.dict())
    await database.execute(query)
    return {**up_order.dict(), 'id': order_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users_table.delete().where(users_table.c.id == user_id)
    await database.execute(query)
    return {'message': f'User_{user_id} deleted'}


@app.delete('/goods/{goods_id}')
async def delete_gds(goods_id: int):
    query = goods_table.delete().where(goods_table.c.id == goods_id)
    await database.execute(query)
    return {'message': f'Product_{goods_id} deleted'}


@app.delete('/orders/{order_id}')
async def delete_order(order_id: int):
    query = orders_table.delete().where(orders_table.c.id == order_id)
    await database.execute(query)
    return {'message': f'Order_{order_id} deleted'}
