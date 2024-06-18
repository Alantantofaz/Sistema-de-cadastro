import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='clientes.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            telefone TEXT,
            procedimento TEXT,
            valor_pago REAL,
            metodo_pagamento TEXT,
            lucro REAL,
            data_cadastro TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_cliente(self, nome, telefone, procedimento, valor_pago, metodo_pagamento, lucro):
        data_cadastro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = '''
        INSERT INTO clientes (nome, telefone, procedimento, valor_pago, metodo_pagamento, lucro, data_cadastro)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (nome, telefone, procedimento, valor_pago, metodo_pagamento, lucro, data_cadastro))
        self.conn.commit()

    def list_clientes(self):
        query = 'SELECT * FROM clientes'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def delete_cliente(self, cliente_id):
        query = 'DELETE FROM clientes WHERE id = ?'
        self.conn.execute(query, (cliente_id,))
        self.conn.commit()

    def calculate_lucro(self, data_inicio, data_fim):
        query = '''
        SELECT SUM(lucro) FROM clientes
        WHERE data_cadastro BETWEEN ? AND ?
        '''
        cursor = self.conn.execute(query, (data_inicio, data_fim))
        result = cursor.fetchone()
        return result[0] if result[0] else 0.0
