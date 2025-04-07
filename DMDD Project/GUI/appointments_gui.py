import tkinter as tk
from tkinter import messagebox, ttk
import database


class AppointmentsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointments Management")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.setup_treeview()
        self.load_appointments()

    def setup_treeview(self):
        columns = ("Appointment_ID", "Patient_ID", "Doctor_ID", "Appointment_Date", "Appointment_Time", "Appointment_Status")
        self.appointments_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        for column in columns:
            self.appointments_tree.heading(column, text=column.replace('_', ' '))
            self.appointments_tree.column(column, width=100)

        self.appointments_tree.pack(fill=tk.BOTH, expand=True)

    def load_appointments(self):
        for i in self.appointments_tree.get_children():
            self.appointments_tree.delete(i)
        for appointment in self.fetch_appointments():
            self.appointments_tree.insert('', 'end', values=(
                appointment["Appointment_ID"], appointment["Patient_ID"],
                appointment["Doctor_ID"], appointment["Appointment_Date"],
                appointment["Appointment_Time"], appointment["Appointment_Status"]
            ))

    def fetch_appointments(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Appointment_ID, Patient_ID, Doctor_ID, Appointment_Date, Appointment_Time, Appointment_Status FROM Appointment")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentsGUI(root)
    root.mainloop()
