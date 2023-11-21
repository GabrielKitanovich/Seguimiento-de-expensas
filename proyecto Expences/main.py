import tkinter
from tkinter import ttk
from functions import *
def on_tab_change(event):
    current_tab = notebook.index(notebook.select())
def tabPrincipalFiller(tab):
    tab.grid()
    label1 = ttk.Label(tab, text = "Seguimiento de Expensas", font= "helvetica")
    label1.pack()
    textbox = ttk.Entry(tab)
    textbox.grid(row=2, column=2)
    textbox.pack()
window = tkinter.Tk()
window.minsize(1280, 720)
window.resizable(0, 0)
window.title("Aplicación de seguimiento de expensas")
window.grid()
notebook = ttk.Notebook(window)

# Crear pestañas
tabPrincipal = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tabPrincipalFiller(tabPrincipal)

# Agregar pestañas al notebook
notebook.add(tabPrincipal, text="Principal")
notebook.add(tab2, text="Pestaña 2")
notebook.add(tab3, text="Pestaña 3")

# Configurar eventos de cambio de pestaña
notebook.bind("<<NotebookTabChanged>>", on_tab_change)

# Pack el notebook para mostrarlo en la ventana principal
notebook.pack(expand=1, fill="both")

window.mainloop()
