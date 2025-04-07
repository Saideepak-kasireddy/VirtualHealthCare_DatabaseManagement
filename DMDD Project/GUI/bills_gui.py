import tkinter as tk
from tkinter import messagebox, ttk
import database


class BillsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bills Management")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.setup_treeview()
        self.load_bills()

    def setup_treeview(self):
        columns = ("Bill_ID", "Prescription_ID", "IssueDate", "TotalAmount", "Status")
        self.bills_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        for column in columns:
            self.bills_tree.heading(column, text=column.replace('_', ' '))
            self.bills_tree.column(column, width=100)

        self.bills_tree.pack(fill=tk.BOTH, expand=True)

    def load_bills(self):
        for i in self.bills_tree.get_children():
            self.bills_tree.delete(i)
        for bill in self.fetch_bills():
            self.bills_tree.insert('', 'end', values=(
                bill["Bill_ID"], bill["Prescription_ID"],
                bill["IssueDate"], bill["TotalAmount"], bill["Status"]
            ))

    def fetch_bills(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Bill_ID, Prescription_ID, IssueDate, TotalAmount, Status FROM Bill")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = BillsGUI(root)
    root.mainloop()
