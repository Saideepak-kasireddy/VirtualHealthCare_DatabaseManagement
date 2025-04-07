import pyodbc
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ===========================
# Database Connection
# ===========================
def get_connection():
    """
    Establishes a connection to the database.
    Adjust the connection string as per your database configuration.
    """
    try:
        return pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=ANJANA;"
            "Database=Virtual_Healthcare;"
            "Trusted_Connection=yes;"
            "Encrypt=Yes;"
            "TrustServerCertificate=Yes;"
        )
    except pyodbc.Error as e:
        logging.error(f"Error connecting to the database: {e}")
        raise


# ===========================
# Utility Function: Fetch View
# ===========================
def fetch_view(view_name):
    """Fetches all records from a specified database view."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {view_name}"
            cursor.execute(query)
            data = cursor.fetchall()
        return data
    except pyodbc.Error as e:
        logging.error(f"Error fetching data from {view_name}: {e}")
        raise


# ===========================
# Patients CRUD Operations
# ===========================
def fetch_patients():
    """Retrieves all patient records from the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC spRetrievePatients")
            return cursor.fetchall()
    except pyodbc.Error as e:
        logging.error(f"Error fetching patients: {e}")
        raise

def add_patient(name, dob, contact, email, user_id, password, insurance_id, address):
    """Adds a new patient to the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Patient (Patient_Name, Patient_DOB, Patient_Contact_Number, Patient_Email, 
                                     Patient_User_ID, Patient_Password, Insurance_ID, Patient_Address)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (name, dob, contact, email, user_id, password, insurance_id, address))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error adding patient: {e}")
        raise

def update_patient(patient_id, name, dob, contact, email, user_id, password, insurance_id, address):
    """Updates an existing patient's information."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Patient
                SET Patient_Name = ?, Patient_DOB = ?, Patient_Contact_Number = ?, Patient_Email = ?, 
                    Patient_User_ID = ?, Patient_Password = ?, Insurance_ID = ?, Patient_Address = ?
                WHERE Patient_ID = ?
            """, (name, dob, contact, email, user_id, password, insurance_id, address, patient_id))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error updating patient: {e}")
        raise

def delete_patient(patient_id):
    """Deletes a patient from the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Patient WHERE Patient_ID = ?", (patient_id,))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error deleting patient: {e}")
        raise


# ===========================
# Doctors CRUD Operations
# ===========================
def fetch_doctors():
    """Retrieves all doctor records from the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC spRetrieveDoctors")
            return cursor.fetchall()
    except pyodbc.Error as e:
        logging.error(f"Error fetching doctors: {e}")
        raise

def add_doctor(name, contact, specialty, availability, department_id, password):
    """Adds a new doctor to the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Doctor (Doctor_Name, Doctor_Contact, Doctor_Specialty, Doctor_Availability, Department_ID, Doctor_Password)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, contact, specialty, availability, department_id, password))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error adding doctor: {e}")
        raise

def update_doctor(doctor_id, name, contact, specialty, availability, department_id, password):
    """Updates an existing doctor's information."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Doctor
                SET Doctor_Name = ?, Doctor_Contact = ?, Doctor_Specialty = ?, Doctor_Availability = ?, 
                    Department_ID = ?, Doctor_Password = ?
                WHERE Doctor_ID = ?
            """, (name, contact, specialty, availability, department_id, password, doctor_id))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error updating doctor: {e}")
        raise

def delete_doctor(doctor_id):
    """Deletes a doctor from the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Doctor WHERE Doctor_ID = ?", (doctor_id,))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error deleting doctor: {e}")
        raise


# ===========================
# Appointments CRUD Operations
# ===========================
def fetch_appointments():
    """Retrieves all appointment records from the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC spRetrieveAppointments")
            return cursor.fetchall()
    except pyodbc.Error as e:
        logging.error(f"Error fetching appointments: {e}")
        raise

def add_appointment(patient_id, doctor_id, date, time, status):
    """Adds a new appointment record to the database."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC spInsertAppointment ?, ?, ?, ?, ?", (patient_id, doctor_id, date, time, status))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error adding appointment: {e}")
        raise

def update_appointment(appointment_id, patient_id, doctor_id, date, time, status):
    """Updates an existing appointment record."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC spUpdateAppointment ?, ?, ?, ?, ?, ?", (appointment_id, patient_id, doctor_id, date, time, status))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error updating appointment: {e}")
        raise

def delete_appointment(appointment_id):
    """Deletes an appointment record."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC spDeleteAppointment ?", (appointment_id,))
            conn.commit()
    except pyodbc.Error as e:
        logging.error(f"Error deleting appointment: {e}")
        raise
