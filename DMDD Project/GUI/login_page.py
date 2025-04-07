import tkinter as tk
from tkinter import messagebox
from dashboard import Dashboard
from doctors_gui import DoctorsGUI  # Import the Doctors GUI
# from dashboard import Dashboard  # Import the Dashboard class from dashboard.py
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Set background color
        self.root.configure(bg="lightblue")

        # Create labels and entries
        self.username_label = tk.Label(root, text="Username:", bg="#f0f0f0", font=("Helvetica", 12))
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="black", bd=2, relief=tk.SOLID)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text="Password:", bg="#f0f0f0", font=("Helvetica", 12))
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(root, show="*", font=("Helvetica", 12), bg="white", fg="black", bd=2, relief=tk.SOLID)
        self.password_entry.pack(pady=5)

        # Create login button
        self.login_button = tk.Button(root, text="Login", command=self.login, font=("Helvetica", 12), bg="lightblue", fg="black", bd=2, relief=tk.RAISED)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.open_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_dashboard(self):
        self.root.destroy()  # Close the login window
        root = tk.Tk()
        root.configure(bg="#f0f0f0")  # Set background color for the dashboard window
        dashboard = Dashboard(root)  # Open the Dashboard
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()