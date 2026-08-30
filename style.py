import tkinter as tk
from tkinter import ttk

def aplicar_estilo(root: tk.Tk):
    style = ttk.Style(root)
    
    try:
        style.theme_use('clam')
        
    except tk.TclError:
        pass
    
    fonte_padrao = ("Segoe UI", 10)
    root.option_add("*Font", fonte_padrao)
    
    style.configure("TLabel", padding=(2, 2))
    style.configure("TEntry", padding=(4, 4))
    style.configure("TButton", padding=(6,4))   
    style.configure("TLabelframe", padding=(8, 8))
    style.configure("TLabelframe.Label", font=("Segoe UI Semibold", 10))
    style.configure("Treeview.Heading", font=("Segoe UI", 10))
  
def aplicar_zebra_treeview(treeview: ttk.Treeview):
    treeview.tag_configure("oddrow", background="#F7F7F7")
    treeview.tag_configure("evenrow", background="#ffffff")   


def preecher_treeview_com_zebra(treeview: ttk.Treeview, rows):
    for i in treeview.get_children():
        treeview.delete(i)

    for idx, row in enumerate(rows):
        tag = "evenrow" if idx % 2 == 0 else "oddrow"
        treeview.insert("", "end", values=row, tags=(tag,))