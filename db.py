import sqlite3
from config import DB_CONFIG


def conectar(usar_banco: bool = False) -> sqlite3.Connection | None:
    """
    Cria conexão com o banco SQLite definido em config.py
    """
    if usar_banco:
        return sqlite3.connect(DB_CONFIG["database"])
    else:
        return None


def criar_banco_e_tabela() -> None:
    """
    Cria a tabela 'pessoas' caso não exista
    """
    conn = conectar(usar_banco=True)
    if conn is None:
        raise RuntimeError("Não foi possível conectar ao banco de dados.")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefone TEXT NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()
