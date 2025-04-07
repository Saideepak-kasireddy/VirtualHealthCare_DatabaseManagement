import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import database


# Utility functions
def validate_date(date_text):
    """Validates the date format."""
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_email(email):
    """Simple email validation."""
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


class PatientsGUI:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.root.title("Patient Management System")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.setup_entry_fields()
        self.setup_operation_buttons()
        self.setup_treeview()
        self.load_patients()
        self.apply_styling()

    def apply_styling(self):
        self.root.config(bg="lightblue")
        self.frame.config(bg="lightblue")
        self.style.configure('TButton', font=('Helvetica', 12), borderwidth='4')
        self.style.map('TButton', foreground=[('pressed', 'red'), ('active', 'blue')],
                       background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        self.style.configure('TEntry', foreground='blue', background='white')
        self.style.configure('Treeview', background='lightblue', foreground='black', rowheight=25)
        self.style.map('Treeview', background=[('selected', 'black')])

    def setup_entry_fields(self):
        labels = {
            "Patient_Name": "Patient Name:",
            "Patient_DOB": "Date of Birth (YYYY-MM-DD):",
            "Patient_Contact_Number": "Contact Number:",
            "Patient_Email": "Email:",
            "Patient_User_ID": "User ID:",
            "Patient_Password": "Password:",
            "Insurance_ID": "Insurance ID:",
            "Patient_Address": "Address:"
        }

        self.entry_widgets = {}
        self.entry_frame = ttk.Frame(self.frame)
        self.entry_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for field_name, label_text in labels.items():
            label = ttk.Label(self.entry_frame, width=25, justify='center', text=label_text)
            label.pack(side=tk.TOP, padx=5, pady=2)

            if field_name == "Patient_Password":
                entry = ttk.Entry(self.entry_frame, width=25, justify='center', show="*")
            else:
                entry = ttk.Entry(self.entry_frame, width=25, justify='center')
            entry.pack(side=tk.TOP, padx=5, pady=2)
            self.entry_widgets[field_name] = entry

    def setup_operation_buttons(self):
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(side=tk.TOP)

        self.add_button = ttk.Button(self.button_frame, text="Add Patient", command=self.add_patient)
        self.add_button.pack(side=tk.TOP, padx=5, pady=5)

        self.update_button = ttk.Button(self.button_frame, text="Update Selected Patient", command=self.update_patient)
        self.update_button.pack(side=tk.TOP, padx=5, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Selected Patient", command=self.delete_patient)
        self.delete_button.pack(side=tk.TOP, padx=5, pady=5)

    def setup_treeview(self):
        columns = (
            "Patient_ID", "Patient_Name", "Patient_DOB", "Patient_Contact_Number",
            "Patient_Email", "Patient_User_ID", "Patient_Password", "Insurance_ID", "Patient_Address"
        )
        self.patients_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        # Configure the columns
        for column in columns:
            self.patients_tree.heading(column, text=column.replace('_', ' '))
            self.patients_tree.column(column, width=100)

        self.patients_tree.pack(fill=tk.BOTH, expand=True)

    def add_patient(self):
        try:
            name = self.entry_widgets["Patient_Name"].get()
            dob = self.entry_widgets["Patient_DOB"].get()
            contact = self.entry_widgets["Patient_Contact_Number"].get()
            email = self.entry_widgets["Patient_Email"].get()
            user_id = self.entry_widgets["Patient_User_ID"].get()
            password = self.entry_widgets["Patient_Password"].get()
            insurance_id = self.entry_widgets["Insurance_ID"].get()
            address = self.entry_widgets["Patient_Address"].get()

            # Validate inputs
            if not validate_date(dob):
                messagebox.showerror("Error", "Date of Birth must be in YYYY-MM-DD format.")
                return
            if not validate_email(email):
                messagebox.showerror("Error", "Invalid email format.")
                return

            database.add_patient(name, dob, contact, email, user_id, password, insurance_id, address)
            self.load_patients()
            messagebox.showinfo("Success", "Patient added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add patient: {e}")

    def update_patient(self):
        selected_items = self.patients_tree.selection()
        if not selected_items:
            messagebox.showinfo("Update Patient", "Please select a patient to update.")
            return

        selected_item = selected_items[0]
        patient_id = self.patients_tree.item(selected_item)["values"][0]

        name = self.entry_widgets["Patient_Name"].get()
        dob = self.entry_widgets["Patient_DOB"].get()
        contact = self.entry_widgets["Patient_Contact_Number"].get()
        email = self.entry_widgets["Patient_Email"].get()
        user_id = self.entry_widgets["Patient_User_ID"].get()
        password = self.entry_widgets["Patient_Password"].get()
        insurance_id = self.entry_widgets["Insurance_ID"].get()
        address = self.entry_widgets["Patient_Address"].get()

        try:
            database.update_patient(patient_id, name, dob, contact, email, user_id, password, insurance_id, address)
            self.load_patients()
            messagebox.showinfo("Success", "Patient updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update patient: {e}")

    def delete_patient(self):
        selected_items = self.patients_tree.selection()
        if not selected_items:
            messagebox.showinfo("Delete Patient", "Please select a patient to delete.")
            return

        selected_item = selected_items[0]
        patient_id = self.patients_tree.item(selected_item)["values"][0]

        try:
            database.delete_patient(patient_id)
            self.load_patients()
            messagebox.showinfo("Success", "Patient deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete patient: {e}")

    def load_patients(self):
        for i in self.patients_tree.get_children():
            self.patients_tree.delete(i)
        for patient in self.fetch_patients():
            self.patients_tree.insert('', 'end', values=(
                patient["Patient_ID"], patient["Patient_Name"], patient["Patient_DOB"],
                patient["Patient_Contact_Number"], patient["Patient_Email"], patient["Patient_User_ID"],
                patient["Patient_Password"], patient["Insurance_ID"], patient["Patient_Address"]
            ))

    def fetch_patients(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    Patient_ID, Patient_Name, Patient_DOB, Patient_Contact_Number, 
                    Patient_Email, Patient_User_ID, Patient_Password, Insurance_ID, Patient_Address
                FROM Patient
            """)
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = PatientsGUI(root)
    root.mainloop()
