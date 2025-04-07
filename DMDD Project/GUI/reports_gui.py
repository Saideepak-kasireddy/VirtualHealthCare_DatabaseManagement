# this will be reports GUI
import tkinter as tk
from tkinter import ttk
import database


class ReportsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Reports")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.setup_treeview()
        self.load_reports()

    def setup_treeview(self):
        columns = ("Record_ID", "Patient_ID", "Blood_Type", "Diagnosis", "Treatment_Plan", "Date")
        self.reports_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        for column in columns:
            self.reports_tree.heading(column, text=column.replace('_', ' '))
            self.reports_tree.column(column, width=100)

        self.reports_tree.pack(fill=tk.BOTH, expand=True)

    def load_reports(self):
        for i in self.reports_tree.get_children():
            self.reports_tree.delete(i)
        for record in self.fetch_reports():
            self.reports_tree.insert('', 'end', values=(
                record["Record_ID"], record["Patient_ID"], record["Blood_Type"],
                record["Diagnosis"], record["Treatment_Plan"], record["Date"]
            ))

    def fetch_reports(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Record_ID, Patient_ID, Blood_Type, Diagnosis, Treatment_Plan, Date FROM Medical_Record")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = ReportsGUI(root)
    root.mainloop()
