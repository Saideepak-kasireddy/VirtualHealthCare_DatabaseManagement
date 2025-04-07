import tkinter as tk
from tkinter import messagebox, ttk
import database


class DoctorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctors Management")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.setup_entry_fields()
        self.setup_operation_buttons()
        self.setup_treeview()
        self.load_doctors()

    def setup_entry_fields(self):
        labels = {
            "Doctor_Name": "Doctor Name:",
            "Doctor_Contact": "Contact:",
            "Doctor_Specialty": "Specialty:",
            "Doctor_Availability": "Availability:",
            "Department_ID": "Department ID:",
            "Doctor_Password": "Password:"
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

        self.add_button = ttk.Button(self.button_frame, text="Add Doctor", command=self.add_doctor)
        self.add_button.pack(side=tk.TOP, padx=5, pady=5)

        self.update_button = ttk.Button(self.button_frame, text="Update Selected Doctor", command=self.update_doctor)
        self.update_button.pack(side=tk.TOP, padx=5, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Selected Doctor", command=self.delete_doctor)
        self.delete_button.pack(side=tk.TOP, padx=5, pady=5)

    def setup_treeview(self):
        columns = ("Doctor_ID", "Doctor_Name", "Doctor_Contact", "Doctor_Specialty", "Doctor_Availability", "Department_ID", "Doctor_Password")
        self.doctors_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        for column in columns:
            self.doctors_tree.heading(column, text=column.replace('_', ' '))
            self.doctors_tree.column(column, width=100)

        self.doctors_tree.pack(fill=tk.BOTH, expand=True)

    def add_doctor(self):
        try:
            name = self.entry_widgets["Doctor_Name"].get()
            contact = self.entry_widgets["Doctor_Contact"].get()
            specialty = self.entry_widgets["Doctor_Specialty"].get()
            availability = self.entry_widgets["Doctor_Availability"].get()
            department_id = int(self.entry_widgets["Department_ID"].get())
            password = self.entry_widgets["Doctor_Password"].get()

            database.add_doctor(name, contact, specialty, availability, department_id, password)
            self.load_doctors()
            messagebox.showinfo("Success", "Doctor added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add doctor: {e}")

    def update_doctor(self):
        selected_items = self.doctors_tree.selection()
        if not selected_items:
            messagebox.showinfo("Update Doctor", "Please select a doctor to update.")
            return

        selected_item = selected_items[0]
        doctor_id = self.doctors_tree.item(selected_item)["values"][0]

        try:
            name = self.entry_widgets["Doctor_Name"].get()
            contact = self.entry_widgets["Doctor_Contact"].get()
            specialty = self.entry_widgets["Doctor_Specialty"].get()
            availability = self.entry_widgets["Doctor_Availability"].get()
            department_id = int(self.entry_widgets["Department_ID"].get())
            password = self.entry_widgets["Doctor_Password"].get()

            database.update_doctor(doctor_id, name, contact, specialty, availability, department_id, password)
            self.load_doctors()
            messagebox.showinfo("Success", "Doctor updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update doctor: {e}")

    def delete_doctor(self):
        selected_items = self.doctors_tree.selection()
        if not selected_items:
            messagebox.showinfo("Delete Doctor", "Please select a doctor to delete.")
            return

        selected_item = selected_items[0]
        doctor_id = self.doctors_tree.item(selected_item)["values"][0]

        try:
            database.delete_doctor(doctor_id)
            self.load_doctors()
            messagebox.showinfo("Success", "Doctor deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete doctor: {e}")

    def load_doctors(self):
        for i in self.doctors_tree.get_children():
            self.doctors_tree.delete(i)
        for doctor in self.fetch_doctors():
            self.doctors_tree.insert('', 'end', values=(
                doctor["Doctor_ID"],
                doctor["Doctor_Name"],
                doctor["Doctor_Contact"],
                doctor["Doctor_Specialty"],
                doctor["Doctor_Availability"],
                doctor["Department_ID"],
                doctor["Doctor_Password"]
            ))

    def fetch_doctors(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Doctor_ID, Doctor_Name, Doctor_Contact, Doctor_Specialty, Doctor_Availability, Department_ID, Doctor_Password FROM Doctor")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = DoctorsGUI(root)
    root.mainloop()
