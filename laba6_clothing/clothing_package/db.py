import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self):
        self.conn_params = {
            'dbname': 'clothing_calc',
            'user': 'postgres',
            'password': 'mysecretpassword',
            'host': 'localhost',
            'port': '5432'
        }
        self._create_table()

    def _get_connection(self):
        return psycopg2.connect(**self.conn_params)

    def _create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS calculations (
            id SERIAL PRIMARY KEY,
            clothing_type VARCHAR(50),
            size INTEGER,
            total_cost NUMERIC(10, 2),
            details JSONB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(create_table_query)
                    conn.commit()
                    print("Таблица 'calculations' успешно создана или уже существует.")
        except Exception as e:
            print(f"Ошибка при создании таблицы: {e}")

    def save_result(self, result_data: dict):
        if 'coat' in result_data:
            clothing_type = result_data['type']
            total_cost = result_data['total']
        else:
            clothing_type = result_data['type']
            total_cost = result_data['total']

        insert_query = """
        INSERT INTO calculations (clothing_type, size, total_cost, details)
        VALUES (%s, %s, %s, %s);
        """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(insert_query, (clothing_type, result_data['size'], total_cost, psycopg2.extras.Json(result_data)))
                    conn.commit()
                    print(f"Результат для {clothing_type} (размер {result_data['size']}) сохранён в БД.")
                    return True
        except Exception as e:
            print(f"Ошибка при сохранении в БД: {e}")
            return False