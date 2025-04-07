import tkinter as tk
from tkinter import messagebox, ttk
import database


class ConsultationRoomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Consultation Room Management")
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.setup_entry_fields()
        self.setup_operation_buttons()
        self.setup_treeview()
        self.load_rooms()

    def setup_entry_fields(self):
        labels = {
            "Appointment_ID": "Appointment ID:",
            "Platform": "Platform:",
            "Room_Status": "Room Status (Available/In session):",
            "Access_Code": "Access Code:",
            "Start_Time": "Start Time (HH:MM:SS):",
            "End_Time": "End Time (HH:MM:SS):"
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

        self.add_button = ttk.Button(self.button_frame, text="Add Room", command=self.add_room)
        self.add_button.pack(side=tk.TOP, padx=5, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Selected Room", command=self.delete_room)
        self.delete_button.pack(side=tk.TOP, padx=5, pady=5)

    def setup_treeview(self):
        columns = ("Room_ID", "Appointment_ID", "Platform", "Room_Status", "Access_Code", "Start_Time", "End_Time")
        self.rooms_tree = ttk.Treeview(self.frame, columns=columns, show="headings")

        for column in columns:
            self.rooms_tree.heading(column, text=column.replace('_', ' '))
            self.rooms_tree.column(column, width=100)

        self.rooms_tree.pack(fill=tk.BOTH, expand=True)

    def add_room(self):
        try:
            appointment_id = int(self.entry_widgets["Appointment_ID"].get())
            platform = self.entry_widgets["Platform"].get()
            room_status = self.entry_widgets["Room_Status"].get()
            access_code = self.entry_widgets["Access_Code"].get()
            start_time = self.entry_widgets["Start_Time"].get()
            end_time = self.entry_widgets["End_Time"].get()

            database.add_consultation_room(appointment_id, platform, room_status, access_code, start_time, end_time)
            self.load_rooms()
            messagebox.showinfo("Success", "Room added successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add room: {e}")

    def delete_room(self):
        selected_items = self.rooms_tree.selection()
        if not selected_items:
            messagebox.showinfo("Delete Room", "Please select a room to delete.")
            return

        selected_item = selected_items[0]
        room_id = self.rooms_tree.item(selected_item)["values"][0]

        try:
            database.delete_consultation_room(room_id)
            self.load_rooms()
            messagebox.showinfo("Success", "Room deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete room: {e}")

    def load_rooms(self):
        for i in self.rooms_tree.get_children():
            self.rooms_tree.delete(i)
        for room in self.fetch_rooms():
            self.rooms_tree.insert('', 'end', values=(
                room["Room_ID"], room["Appointment_ID"], room["Platform"],
                room["Room_Status"], room["Access_Code"], room["Start_Time"], room["End_Time"]
            ))

    def fetch_rooms(self):
        with database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Room_ID, Appointment_ID, Platform, Room_Status, Access_Code, Start_Time, End_Time FROM Consultation_Room")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


if __name__ == "__main__":
    root = tk.Tk()
    app = ConsultationRoomGUI(root)
    root.mainloop()
