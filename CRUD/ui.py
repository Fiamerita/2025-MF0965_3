import tkinter as tk
from tkinter import ttk, messagebox
from customer_service import CustomerService


class WorldUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Clientes - World")
        self.service = CustomerService()
        self._build_ui()
        self._load_customers()

    def _build_ui(self):
        cols = ('Code', 'Nombre', 'Poblacion', 'Capital', 'Poblacion capital')
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frm = tk.Frame(self.root); frm.pack(pady=10)
        tk.Button(frm, text="Añadir",    command=self._on_add).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Editar",    command=self._on_edit).pack(side=tk.LEFT, padx=5)
    

    def _load_customers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for cust in self.service.list_customers():
            self.tree.insert('', tk.END, values=cust)

    def _on_add(self):
        return self.formulario()


    def _on_edit(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Editar", "Seleccione un cliente")
            return
        self.formulario()
    
    def formulario(self):
        add_win = tk.Toplevel(self.root)
        add_win.title("Añadir nuevo país")
        fields = ['Code', 'Nombre','Continente','Region','Area','IndepYear', 'Población', 'ExpecVida', 'GNP', 'GNPOld', 'NombreLocal', 'FormaGob', 'Alcalde', 'capital', 'Code2']
        entries = {}
        for i, field in enumerate(fields):
            tk.Label(add_win, text=field).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            entry = tk.Entry(add_win)
            entry.grid(row=i, column=1, padx=5, pady=2)
            entries[field] = entry

        def save():
            values = [entries[f].get() for f in fields]
            if not values[0]:
                messagebox.showwarning("Error", "El campo 'Code' es obligatorio")
                return
            self.service.add_customer(tuple(values))
            self._load_customers()
            add_win.destroy()

        tk.Button(add_win, text="Guardar", command=save).grid(row=len(fields), column=0, columnspan=2, pady=10)


    def _on_delete(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Eliminar", "Seleccione un cliente")
            return
        cust_id = self.tree.item(sel, 'values')[0]
        if messagebox.askyesno("Eliminar", "¿Confirmar?"):
            self.service.remove_customer(cust_id)
            self._load_customers()