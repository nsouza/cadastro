import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from openpyxl import workbook
from openpyxl.utils import get_column_letter
from db import conectar
from repo import PessoaRepo
from style import aplicar_estilo, aplicar_zebra_treeview, preecher_treeview_com_zebra

def validar(nome: str, email: str, telefone: str):
    if not nome or len(nome.strip()) < 3:
        return False, "Informe um nome com pelo menos 3 caracteres."
    
    if not email or "@" not in email:
        return False, "Informe um e-mail válido (ex.: nome@domininio.com)."
    
    if not telefone or len(telefone.strip()) < 6:
        return False, "Informe um telefone válido."
    
    return True, ""
        

class AppCadastro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Pessoas - TKinter + SQlite3")
        self.geometry("980x580")
        self.minsize(900,520)
        aplicar_estilo(self)
        self.conn = conectar(usar_banco=True)