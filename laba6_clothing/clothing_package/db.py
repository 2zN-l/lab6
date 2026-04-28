import sqlite3
import json
import os

class DatabaseManager:
    def __init__(self):
        self.db_path = 'clothing_calc.db'
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            clothing_type VARCHAR(50),
            size INTEGER,
            total_cost REAL,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            with self._get_connection() as conn:
                conn.execute(create_table_query)
                conn.commit()
        except Exception as e:
            print(f"Ошибка при создании таблицы: {e}")

    def save_result(self, result_data: dict) -> bool:
        if 'coat' in result_data:
            clothing_type = result_data['type']
            total_cost = result_data['total']
        else:
            clothing_type = result_data['type']
            total_cost = result_data['total']

        insert_query = """
        INSERT INTO calculations (clothing_type, size, total_cost, details)
        VALUES (?, ?, ?, ?);
        """
        try:
            with self._get_connection() as conn:
                conn.execute(insert_query, (
                    clothing_type, 
                    result_data['size'], 
                    total_cost, 
                    json.dumps(result_data, ensure_ascii=False)
                ))
                conn.commit()
                print(f"Результат для {clothing_type} (размер {result_data['size']}) сохранён")
                return True
        except Exception as e:
            print(f"Ошибка при сохранении в БД: {e}")
            return False

    def get_all_results(self) -> list:
        try:
            with self._get_connection() as conn:
                cursor = conn.execute("""
                    SELECT id, clothing_type, size, total_cost, created_at 
                    FROM calculations 
                    ORDER BY created_at DESC
                """)
                return cursor.fetchall()
        except Exception as e:
            print(f"Ошибка при получении результатов: {e}")
            return []

    def get_result_by_id(self, result_id: int) -> dict:
        try:
            with self._get_connection() as conn:
                cursor = conn.execute("""
                    SELECT id, clothing_type, size, total_cost, details, created_at 
                    FROM calculations 
                    WHERE id = ?
                """, (result_id,))
                row = cursor.fetchone()
                if row:
                    return {
                        'id': row[0],
                        'clothing_type': row[1],
                        'size': row[2],
                        'total_cost': row[3],
                        'details': json.loads(row[4]),
                        'created_at': row[5]
                    }
                return None
        except Exception as e:
            print(f"Ошибка при получении результата по ID: {e}")
            return None