from typing import List, Tuple
from config import DB_CONFIG

class PessoaRepo:
    
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
        
    def inserir(self, nome:str, email:str, telefone:str) -> None:
        self.cur.execute(
            f"INSERT INTO {DB_CONFIG['nome_tabela']} (nome, email, telefone) VALUES (%s, %s, %s)",
            (nome, email, telefone)
        )
        
    def listar_todos(self) -> List[Tuple]:
        self.cur.execute(
            f"SELECT id, nome, email, telefone, criado_em FROM {DB_CONFIG['nome_tabela']} ORDER BY id DESC;"
            f"FROM {DB_CONFIG['nome_tabela']} ORDER BY id DESC"
        )
        return self.cur.fetchall()
    
    def pesquisar(self, termo:str ) -> List[Tuple]:
        like = f"%{termo}%"
        self.cur.execute(
            f"""
                SELECT id, nome, emai, telefone, criado_em
                FROM {DB_CONFIG['nome_tabela']}
                WHERE nome LIKE %s OR email LIKE %s OR telefone LIKE %S
                ORDER BY id DESC
            """,
                (like, like, like),            
        )
        return self.cur.fetchall()
    
    def atualizar(self, id_:int, nome:str, email:str, telefone:str) -> None:
        self.cur.execute(
            f"UPDATE {DB_CONFIG['nome_tabela']} SET nome=%s, telefone=%s WHERE id=%s",
            (nome, email, telefone, id_)
        )
    
    def excluir(self, id_: int) -> None:
        self.cur.execute(
            f"DELETE FROM {DB_CONFIG['nome_tabela']} WHERE id=%s",
            (id_,)
        )
        