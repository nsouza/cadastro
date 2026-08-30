import sqlite3
from config import DB_CONFIG

def conectar():
    return sqlite3.connect(DB_CONFIG["database"])

def criar_banco_e_tabela():
    conn = conectar()
    cursor = conn.cursor()
    
    # Exemplo de criação de tabela
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {DB_CONFIG["database"]} " 
        "DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;"
        """)
    
    # Exemplo de criação de tabela
    cursor.execute(
        f"""
            CREATE TABLE IF NOT EXISTS {DB_CONFIG["database"]} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                telefone VARCHAR(20) NOT NULL
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """)
    
    conn.commit()
    conn.close()
