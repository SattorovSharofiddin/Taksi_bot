from loguru import logger

from db import db

async def create_tables():
    users = """create table if not exists users(
        id serial primary key,
        full_name varchar(255) not null,
        tlg_user_id bigint not null unique,
        phone varchar(50) not null unique
    );"""
    cars = """create table if not exists cars(
        id serial primary key,
        name varchar(255) not null
    );"""
    drivers = """create table if not exists drivers(
        id serial primary key,
        user_id int references users(id),
        car_id int references cars(id),
        car_number varchar(15)
    );"""
    active_clients = """create table if not exists active_clients(
        id serial primary key,
        user_id int references users(id),
        "type" varchar(255) not null,
        status varchar(255) not null,
        price varchar(255) not null,
        "from" varchar(255) not null,
        "to" varchar(255) not null,
        passenger_count smallint,
        additional_info text
    );"""
    active_drivers = """create table if not exists active_drivers(
        id serial primary key,
        driver_id int references drivers(id),
        status varchar(255) not null,
        "from" varchar(255) not null,
        "to" varchar(255) not null,
        seats_count smallint not null,
        additional_info text
    );"""

    await db.execute_multiple(users, cars, drivers, active_clients, active_drivers)
    logger.info('ℹ tables successfully created')

async def create_user(data):
    query = """insert into users(tlg_user_id, full_name, phone) values ($1,$2,$3)"""
    await db.pool.execute(query, *data)

async def create_active_driver(data):
    query = """insert into active_drivers(driver_id, status, "from", "to", seats_count, additional_info) values ($1, $2, $3, $4, $5)""" # noqa
    await db.pool.execute(query, *data)

async def create_active_client(data):
    query = """insert into active_clients(user_id, "type", status, "from", "to", passenger_count, additional_info) values ($1, $2, $3, $4, $5, $6)""" # noqa
    await db.pool.execute(query, *data)
