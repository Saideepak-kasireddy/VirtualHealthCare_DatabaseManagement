import tkinter as tk
from tkinter import ttk, messagebox
import database
from datetime import datetime

class ViewReportGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("View Reports")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.setup_buttons()
        self.setup_treeview()

    def setup_buttons(self):
        """Creates buttons for the various report views."""
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(side=tk.TOP, pady=10)

        # Button definitions for each report
        buttons = [
            ("Patient Appointments", self.show_patient_appointments),
            ("Medication Usage and Stock", self.show_medication_usage_stock),
            ("Detailed Prescriptions", self.show_detailed_prescriptions),
        ]

        for idx, (label, command) in enumerate(buttons):
            ttk.Button(self.button_frame, text=label, command=command).grid(row=0, column=idx, padx=5)

    def setup_treeview(self):
        """Initializes the treeview widget for displaying report data."""
        self.tree_frame = ttk.Frame(self.frame)
        self.tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(self.tree_frame, show="headings")
        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.treeview.yview)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.treeview.configure(yscrollcommand=self.tree_scroll.set)

    def clear_treeview(self):
        """Clears the current data and columns in the treeview."""
        self.treeview.delete(*self.treeview.get_children())
        self.treeview["columns"] = ()

    def populate_treeview(self, columns, data):
        """Populates the treeview with data and sets up column headers."""
        self.treeview["columns"] = columns
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150, anchor="center")

        # Format and insert rows
        for row in data:
            formatted_row = self.format_row(row)
            self.treeview.insert("", "end", values=formatted_row)

    def format_row(self, row):
        """Formats the row data to ensure correct display."""
        formatted_row = []
        for item in row:
            if isinstance(item, datetime):
                # Format datetime objects as "MM/DD/YYYY"
                formatted_row.append(item.strftime("%m/%d/%Y"))
            elif isinstance(item, (int, float)):
                # Ensure numeric data is displayed without additional formatting
                formatted_row.append(f"{item}")
            else:
                # Handle strings and other types
                formatted_row.append(str(item).strip("'"))  # Remove any single quotes
        return tuple(formatted_row)

    def show_patient_appointments(self):
        """Fetches and displays data for Patient Appointments."""
        self.clear_treeview()
        columns = ("Patient Name", "Doctor Name", "Appointment Date", "Appointment Time", "Appointment Status")
        self.display_data("vw_PatientAppointments", columns)

    def show_medication_usage_stock(self):
        """Fetches and displays data for Medication Usage and Stock."""
        self.clear_treeview()
        columns = ("Medication ID", "Medication Name", "Description", "Quantity In Stock", "Total Ordered", "Available Stock")
        self.display_data("vw_MedicationUsageStock", columns)

    def show_detailed_prescriptions(self):
        """Fetches and displays data for Detailed Prescriptions."""
        self.clear_treeview()
        columns = ("Prescription ID", "Patient Name", "Doctor Name", "Issue Date", "Medication Name", "Quantity Ordered", "Amount")
        self.display_data("vw_DetailedPrescriptions", columns)

    def display_data(self, view_name, columns):
        """
        Fetches data from the specified database view and populates the treeview.

        Args:
            view_name (str): The name of the database view to fetch data from.
            columns (tuple): The column headers for the treeview.
        """
        try:
            data = database.fetch_view(view_name)
            if not data:
                raise ValueError("No data found in the view.")
            self.populate_treeview(columns, data)
        except Exception as e:
            # Display a meaningful error message
            messagebox.showerror("Error", f"Failed to load data from {view_name}: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ViewReportGUI(root)
    root.mainloop()
