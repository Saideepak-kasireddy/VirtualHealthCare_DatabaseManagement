import tkinter as tk
from doctors_gui import DoctorsGUI  # Import the Doctors GUI
from patients_gui import PatientsGUI  # Import the Patients GUI
from reports_gui import ReportsGUI  # Import the Patient Reports GUI
from prescriptions_gui import PrescriptionsGUI  # Import the Prescriptions GUI
from appointments_gui import AppointmentsGUI  # Import the Appointments GUI
from consultation_room_gui import ConsultationRoomGUI  # Import the Consultation Room GUI
from bills_gui import BillsGUI  # Import the Bills GUI
from feedback_gui import FeedbackGUI  # Import the Feedback GUI
from view_report_gui import ViewReportGUI # Import View Report GUI


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Healthcare Dashboard")
        self.root.geometry("400x600")  # Adjust the size to accommodate all buttons

        # Set the background color
        self.root.config(bg="lightblue")

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root, bg="lightblue")
        self.button_frame.pack(expand=True, fill=tk.BOTH)

        # Define button styling
        button_style = {"font": ("Helvetica", 14), "padx": 20, "pady": 10, "bg": "white", "fg": "black", "relief": "raised"}

        # Create buttons for each module
        self.doctors_button = tk.Button(self.button_frame, text="Doctors & Departments", command=self.open_doctors_gui, **button_style)
        self.doctors_button.pack(expand=True, pady=10)

        self.patients_button = tk.Button(self.button_frame, text="Patients", command=self.open_patients_gui, **button_style)
        self.patients_button.pack(expand=True, pady=10)

        self.patient_report_button = tk.Button(self.button_frame, text="Patient Reports", command=self.open_reports_gui, **button_style)
        self.patient_report_button.pack(expand=True, pady=10)

        self.prescription_button = tk.Button(self.button_frame, text="Prescriptions", command=self.open_prescriptions_gui, **button_style)
        self.prescription_button.pack(expand=True, pady=10)

        self.appointments_button = tk.Button(self.button_frame, text="Appointments", command=self.open_appointments_gui, **button_style)
        self.appointments_button.pack(expand=True, pady=10)

        self.consultation_room_button = tk.Button(self.button_frame, text="Consultation Room", command=self.open_consultation_room_gui, **button_style)
        self.consultation_room_button.pack(expand=True, pady=10)

        self.bills_button = tk.Button(self.button_frame, text="Bills", command=self.open_bills_gui, **button_style)
        self.bills_button.pack(expand=True, pady=10)

        self.feedback_button = tk.Button(self.button_frame, text="Feedback", command=self.open_feedback_gui, **button_style)
        self.feedback_button.pack(expand=True, pady=10)

        self.view_report_button = tk.Button(self.button_frame, text="View Report", command=self.open_view_report_gui, **button_style)
        self.view_report_button.pack(expand=True, pady=10)

        # Center the frame in the window
        self.button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def open_doctors_gui(self):
        """Open the Doctors and Departments GUI."""
        doctors_window = tk.Toplevel(self.root)
        doctors_gui = DoctorsGUI(doctors_window)

    def open_patients_gui(self):
        """Open the Patients GUI."""
        patients_window = tk.Toplevel(self.root)
        patients_gui = PatientsGUI(patients_window)

    def open_reports_gui(self):
        """Open the Patient Reports GUI."""
        reports_window = tk.Toplevel(self.root)
        reports_gui = ReportsGUI(reports_window)

    def open_prescriptions_gui(self):
        """Open the Prescriptions GUI."""
        prescriptions_window = tk.Toplevel(self.root)
        prescriptions_gui = PrescriptionsGUI(prescriptions_window)

    def open_appointments_gui(self):
        """Open the Appointments GUI."""
        appointments_window = tk.Toplevel(self.root)
        appointments_gui = AppointmentsGUI(appointments_window)

    def open_consultation_room_gui(self):
        """Open the Consultation Room GUI."""
        consultation_room_window = tk.Toplevel(self.root)
        consultation_room_gui = ConsultationRoomGUI(consultation_room_window)

    def open_bills_gui(self):
        """Open the Bills GUI."""
        bills_window = tk.Toplevel(self.root)
        bills_gui = BillsGUI(bills_window)

    def open_feedback_gui(self):
        """Open the Feedback GUI."""
        feedback_window = tk.Toplevel(self.root)
        feedback_gui = FeedbackGUI(feedback_window)

    def open_view_report_gui(self):
        """Open the View Report GUI."""
        view_report_window = tk.Toplevel(self.root)
        view_report_gui = ViewReportGUI(view_report_window)


if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()