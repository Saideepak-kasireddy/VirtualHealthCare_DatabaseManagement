import tkinter as tk
from tkinter import messagebox, ttk
import database


class PrescriptionsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Prescriptions Management")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.setup_entry_fields()
        self.setup_operation_buttons()
        self.setup_treeview()
        self.load_prescriptions()

    def setup_entry_fields(self):
        labels = {
            "Patient_ID": "Patient ID:",
            "Doctor_ID": "Doctor ID:",
            "Issue_Date": "Issue Date (YYYY-MM-DD):"
        }

        self.entry_widgets = {}
        self.entry_frame = ttk.Frame(self.frame)
        self.entry_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for field_name, label_text in labels.items():
            label = ttk.Label(self.entry_frame, width=25, text=label_text)
            label.pack(side=tk.TOP, padx=5, pady=2)

            entry = ttk.Entry(self.entry_frame, width=25)
            entry.pack(side=tk.TOP, padx=5, pady=2)
            self.entry_widgets[field_name] = entry

    def setup_operation_buttons(self):
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(side=tk.TOP)

        self.add_button = ttk.Button(self.button_frame, text="Add Prescription", command=self.add_prescription)
        self.add_button.pack(side=tk.TOP, padx=5, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Selected Prescription", command=self.delete_prescription)
        self.delete_button.pack(side=tk.TOP, padx=5, pady=5)

    def setup_treeview(self):
        columns = ("Prescription_ID", "Patient_ID", "Doctor_ID", "Issue_Date")
        self.prescriptions_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        for column in columns:
            self.prescriptions_tree.heading(column, text=column.replace('_', ' '))
            self.prescriptions_tree.column(column, width=100)

        self.prescriptions_tree.pack(fill=tk.BOTH, expand=True)

    def add_prescription(self):
        try:
            patient_id = int(self.entry_widgets["Patient_ID"].get())
            doctor_id = int(self.entry_widgets["Doctor_ID"].get())
            issue_date = self.entry_widgets["Issue_Date"].get()

            database.add_prescription(patient_id, doctor_id, issue_date)
            self.load_prescriptions()
            messagebox.showinfo("Success", "Prescription added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add prescription: {e}")

    def delete_prescription(self):
        selected_items = self.prescriptions_tree.selection()
        if not selected_items:
            messagebox.showinfo("Delete Prescription", "Please select a prescription to delete.")
            return

        selected_item = selected_items[0]
        prescription_id = self.prescriptions_tree.item(selected_item)["values"][0]

        try:
            database.delete_prescription(prescription_id)
            self.load_prescriptions()
            messagebox.showinfo("Success", "Prescription deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete prescription: {e}")

    def load_prescriptions(self):
        for i in self.prescriptions_tree.get_children():
            self.prescriptions_tree.delete(i)
        for prescription in self.fetch_prescriptions():
            self.prescriptions_tree.insert('', 'end', values=(
                prescription["Prescription_ID"], prescription["Patient_ID"],
                prescription["Doctor_ID"], prescription["Issue_Date"]
            ))

    def fetch_prescriptions(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Prescription_ID, Patient_ID, Doctor_ID, Issue_Date FROM Prescription")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = PrescriptionsGUI(root)
    root.mainloop()