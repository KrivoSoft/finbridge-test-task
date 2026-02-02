import os
import psycopg2
from flask import Flask

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'testdb')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASSWORD', 'password')


def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn


@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Создаем таблицу, если её нет (для простоты теста)
        cur.execute('CREATE TABLE IF NOT EXISTS pings (id serial PRIMARY KEY, num integer, data varchar);')

        # Делаем запись (эмуляция полезной работы)
        cur.execute('INSERT INTO pings (num, data) VALUES (%s, %s)', (1, 'Ping!'))

        # Считаем количество записей
        cur.execute('SELECT count(*) FROM pings;')
        count = cur.fetchone()[0]

        conn.commit()
        cur.close()
        conn.close()

        return f"Hello! I have been pinged {count} times directly in PostgreSQL."
    except Exception as e:
        return f"Error connecting to DB: {str(e)}"


if __name__ == '__main__':
    # Слушаем 0.0.0.0, чтобы было доступно извне контейнера
    app.run(host='0.0.0.0', port=5000)