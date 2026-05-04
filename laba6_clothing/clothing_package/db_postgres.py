import psycopg2
import json
from datetime import datetime

class DatabaseManager:
    def __init__(self, host='localhost', port=5432, database='clothing_db', user='postgres', password='123456'):
        self.conn_params = {
            'host': host,
            'port': port,
            'database': database,
            'user': user,
            'password': password
        }
        self._connected = False
        self._init_db()
    
    def _get_connection(self):
        return psycopg2.connect(**self.conn_params)
    
    def _init_db(self):
        try:
            conn = psycopg2.connect(
                host=self.conn_params['host'],
                port=self.conn_params['port'],
                user=self.conn_params['user'],
                password=self.conn_params['password']
            )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{self.conn_params['database']}'")
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(f"CREATE DATABASE {self.conn_params['database']}")
            cursor.close()
            conn.close()
            
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS calculations (
                    id SERIAL PRIMARY KEY,
                    saved_at TEXT,
                    data TEXT
                )
            ''')
            conn.commit()
            cursor.close()
            conn.close()
            self._connected = True
            print("Подключено к PostgreSQL")
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            self._connected = False
    
    def save_result(self, result_data):
        if not self._connected:
            return False
        try:
            if 'saved_at' not in result_data:
                result_data['saved_at'] = datetime.now().isoformat()
            json_data = json.dumps(result_data, ensure_ascii=False)
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO calculations (saved_at, data) VALUES (%s, %s)",
                (result_data['saved_at'], json_data)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False
    
    def get_all_results(self):
        if not self._connected:
            return []
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, saved_at, data FROM calculations ORDER BY id DESC")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            results = []
            for row in rows:
                data = json.loads(row[2])
                data['id'] = row[0]
                data['_id'] = str(row[0])
                data['saved_at'] = row[1]
                results.append(data)
            return results
        except Exception as e:
            print(f"Ошибка получения: {e}")
            return []
    
    def get_result_by_id(self, result_id):
        if not self._connected:
            return None
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, saved_at, data FROM calculations WHERE id = %s", (result_id,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            if row:
                data = json.loads(row[2])
                data['id'] = row[0]
                data['_id'] = str(row[0])
                data['saved_at'] = row[1]
                return data
            return None
        except Exception as e:
            print(f"Ошибка получения: {e}")
            return None