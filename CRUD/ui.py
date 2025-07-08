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
        cols = ('Code', 'Nombre','Poblacion')
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frm = tk.Frame(self.root); frm.pack(pady=10)
        tk.Button(frm, text="Refrescar", command=self._load_customers).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Añadir",    command=self._on_add).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Editar",    command=self._on_edit).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Eliminar",  command=self._on_delete).pack(side=tk.LEFT, padx=5)

    def _load_customers(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for cust in self.service.list_customers():
            self.tree.insert('', tk.END, values=cust)

    def _on_add(self):
        messagebox.showinfo("Añadir", "Implementar formulario de alta aquí")

    def _on_edit(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Editar", "Seleccione un cliente")
            return
        data = self.tree.item(sel, 'values')
        messagebox.showinfo("Editar", f"Implementar edición de {data}")

    def _on_delete(self):
        sel = self.tree.focus()
        if not sel:
            messagebox.showwarning("Eliminar", "Seleccione un cliente")
            return
        cust_id = self.tree.item(sel, 'values')[0]
        if messagebox.askyesno("Eliminar", "¿Confirmar?"):
            self.service.remove_customer(cust_id)
            self._load_customers()
