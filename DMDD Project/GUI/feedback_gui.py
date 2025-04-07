import tkinter as tk
from tkinter import messagebox, ttk
import database


class FeedbackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Feedback Management")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.setup_entry_fields()
        self.setup_operation_buttons()
        self.setup_treeview()
        self.load_feedback()

    def setup_entry_fields(self):
        labels = {
            "Patient_ID": "Patient ID:",
            "Appointment_ID": "Appointment ID:",
            "Rating": "Rating (1-5):",
            "Comments": "Comments:",
            "Feedback_Date": "Feedback Date (YYYY-MM-DD):"
        }

        self.entry_widgets = {}
        self.entry_frame = ttk.Frame(self.frame)
        self.entry_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for field_name, label_text in labels.items():
            label = ttk.Label(self.entry_frame, width=25, text=label_text, anchor="w")
            label.pack(side=tk.TOP, padx=5, pady=2)

            entry = ttk.Entry(self.entry_frame, width=50)
            entry.pack(side=tk.TOP, padx=5, pady=2)
            self.entry_widgets[field_name] = entry

    def setup_operation_buttons(self):
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(side=tk.TOP)

        self.add_button = ttk.Button(self.button_frame, text="Add Feedback", command=self.add_feedback)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.update_button = ttk.Button(self.button_frame, text="Update Feedback", command=self.update_feedback)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Feedback", command=self.delete_feedback)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

    def setup_treeview(self):
        columns = ("Feedback_ID", "Patient_ID", "Appointment_ID", "Rating", "Comments", "Feedback_Date")
        self.feedback_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        for column in columns:
            self.feedback_tree.heading(column, text=column.replace('_', ' '))
            self.feedback_tree.column(column, width=100)

        self.feedback_tree.pack(fill=tk.BOTH, expand=True)

    def validate_rating(self, rating):
        """Validate that the rating is between 1 and 5."""
        try:
            rating = int(rating)
            if 1 <= rating <= 5:
                return True
        except ValueError:
            pass
        return False

    def add_feedback(self):
        try:
            patient_id = self.entry_widgets["Patient_ID"].get()
            appointment_id = self.entry_widgets["Appointment_ID"].get()
            rating = self.entry_widgets["Rating"].get()
            comments = self.entry_widgets["Comments"].get()
            feedback_date = self.entry_widgets["Feedback_Date"].get()

            # Validate rating
            if not self.validate_rating(rating):
                messagebox.showerror("Error", "Rating must be an integer between 1 and 5.")
                return

            database.add_feedback(patient_id, appointment_id, rating, comments, feedback_date)
            self.load_feedback()
            messagebox.showinfo("Success", "Feedback added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add feedback: {e}")

    def update_feedback(self):
        selected_items = self.feedback_tree.selection()
        if not selected_items:
            messagebox.showinfo("Update Feedback", "Please select feedback to update.")
            return

        selected_item = selected_items[0]
        feedback_id = self.feedback_tree.item(selected_item)["values"][0]

        try:
            patient_id = self.entry_widgets["Patient_ID"].get()
            appointment_id = self.entry_widgets["Appointment_ID"].get()
            rating = self.entry_widgets["Rating"].get()
            comments = self.entry_widgets["Comments"].get()
            feedback_date = self.entry_widgets["Feedback_Date"].get()

            # Validate rating
            if not self.validate_rating(rating):
                messagebox.showerror("Error", "Rating must be an integer between 1 and 5.")
                return

            database.update_feedback(feedback_id, patient_id, appointment_id, rating, comments, feedback_date)
            self.load_feedback()
            messagebox.showinfo("Success", "Feedback updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update feedback: {e}")

    def delete_feedback(self):
        selected_items = self.feedback_tree.selection()
        if not selected_items:
            messagebox.showinfo("Delete Feedback", "Please select feedback to delete.")
            return

        selected_item = selected_items[0]
        feedback_id = self.feedback_tree.item(selected_item)["values"][0]

        try:
            database.delete_feedback(feedback_id)
            self.load_feedback()
            messagebox.showinfo("Success", "Feedback deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete feedback: {e}")

    def load_feedback(self):
        for i in self.feedback_tree.get_children():
            self.feedback_tree.delete(i)
        for feedback in self.fetch_feedback():
            self.feedback_tree.insert('', 'end', values=(
                feedback["Feedback_ID"], feedback["Patient_ID"],
                feedback["Appointment_ID"], feedback["Rating"],
                feedback["Comments"], feedback["Feedback_Date"]
            ))

    def fetch_feedback(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Feedback_ID, Patient_ID, Appointment_ID, Rating, Comments, Feedback_Date 
                FROM Feedback
            """)
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackGUI(root)
    root.mainloop()
