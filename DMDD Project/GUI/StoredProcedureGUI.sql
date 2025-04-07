-- ===========================
-- Database: Virtual Healthcare
-- Stored Procedures for CRUD Operations
-- ===========================

-- ===========================
-- Patients Stored Procedures
-- ===========================

-- Procedure to Insert a New Patient
CREATE PROCEDURE spInsertPatient
    @Patient_Name NVARCHAR(100),  -- Patient's Full Name
    @Patient_DOB DATE,           -- Patient's Date of Birth
    @Patient_Contact_Number NVARCHAR(15),  -- Patient's Contact Number
    @Patient_Address NVARCHAR(255)         -- Patient's Address
AS
BEGIN
    INSERT INTO Patient (Patient_Name, Patient_DOB, Patient_Contact_Number, Patient_Address)
    VALUES (@Patient_Name, @Patient_DOB, @Patient_Contact_Number, @Patient_Address);
END;
GO

-- Procedure to Retrieve All Patients
CREATE PROCEDURE spRetrievePatients
AS
BEGIN
    SELECT Patient_ID, Patient_Name, Patient_DOB, Patient_Contact_Number, Patient_Address
    FROM Patient;
END;
GO

-- Procedure to Update an Existing Patient
CREATE PROCEDURE spUpdatePatient
    @Patient_ID INT,                 -- Patient ID to Identify the Record
    @Patient_Name NVARCHAR(100),     -- Updated Name
    @Patient_DOB DATE,               -- Updated Date of Birth
    @Patient_Contact_Number NVARCHAR(15), -- Updated Contact Number
    @Patient_Address NVARCHAR(255)   -- Updated Address
AS
BEGIN
    UPDATE Patient
    SET Patient_Name = @Patient_Name,
        Patient_DOB = @Patient_DOB,
        Patient_Contact_Number = @Patient_Contact_Number,
        Patient_Address = @Patient_Address
    WHERE Patient_ID = @Patient_ID;
END;
GO

-- Procedure to Delete a Patient
CREATE PROCEDURE spDeletePatient
    @Patient_ID INT  -- Patient ID to Identify the Record to be Deleted
AS
BEGIN
    DELETE FROM Patient
    WHERE Patient_ID = @Patient_ID;
END;
GO

-- ===========================
-- Doctors Stored Procedures
-- ===========================

-- Procedure to Insert a New Doctor
CREATE PROCEDURE spInsertDoctor
    @Department_ID INT,             -- Department ID Associated with the Doctor
    @Doctor_Name NVARCHAR(100),     -- Doctor's Full Name
    @Doctor_Contact NVARCHAR(15),   -- Doctor's Contact Number
    @Doctor_Specialty NVARCHAR(50), -- Doctor's Area of Specialty
    @Doctor_Availability NVARCHAR(50) -- Doctor's Availability Status
AS
BEGIN
    INSERT INTO Doctor (Department_ID, Doctor_Name, Doctor_Contact, Doctor_Specialty, Doctor_Availability)
    VALUES (@Department_ID, @Doctor_Name, @Doctor_Contact, @Doctor_Specialty, @Doctor_Availability);
END;
GO

-- Procedure to Retrieve All Doctors
CREATE PROCEDURE spRetrieveDoctors
AS
BEGIN
    SELECT Doctor_ID, Department_ID, Doctor_Name, Doctor_Contact, Doctor_Specialty, Doctor_Availability
    FROM Doctor;
END;
GO

-- Procedure to Update an Existing Doctor
CREATE PROCEDURE spUpdateDoctor
    @Doctor_ID INT,                 -- Doctor ID to Identify the Record
    @Department_ID INT,             -- Updated Department ID
    @Doctor_Name NVARCHAR(100),     -- Updated Name
    @Doctor_Contact NVARCHAR(15),   -- Updated Contact Number
    @Doctor_Specialty NVARCHAR(50), -- Updated Specialty
    @Doctor_Availability NVARCHAR(50) -- Updated Availability Status
AS
BEGIN
    UPDATE Doctor
    SET Department_ID = @Department_ID,
        Doctor_Name = @Doctor_Name,
        Doctor_Contact = @Doctor_Contact,
        Doctor_Specialty = @Doctor_Specialty,
        Doctor_Availability = @Doctor_Availability
    WHERE Doctor_ID = @Doctor_ID;
END;
GO

-- Procedure to Delete a Doctor
CREATE PROCEDURE spDeleteDoctor
    @Doctor_ID INT  -- Doctor ID to Identify the Record to be Deleted
AS
BEGIN
    DELETE FROM Doctor
    WHERE Doctor_ID = @Doctor_ID;
END;
GO

-- ===========================
-- Appointments Stored Procedures
-- ===========================

-- Procedure to Insert a New Appointment
CREATE PROCEDURE spInsertAppointment
    @Patient_ID INT,                -- Patient ID Associated with the Appointment
    @Doctor_ID INT,                 -- Doctor ID Associated with the Appointment
    @Appointment_Date DATE,         -- Appointment Date
    @Appointment_Time TIME,         -- Appointment Time
    @Appointment_Status NVARCHAR(20) -- Appointment Status (e.g., Scheduled, Completed)
AS
BEGIN
    INSERT INTO Appointment (Patient_ID, Doctor_ID, Appointment_Date, Appointment_Time, Appointment_Status)
    VALUES (@Patient_ID, @Doctor_ID, @Appointment_Date, @Appointment_Time, @Appointment_Status);
END;
GO

-- Procedure to Retrieve All Appointments with Patient and Doctor Details
CREATE PROCEDURE spRetrieveAppointments
AS
BEGIN
    SELECT a.Appointment_ID, 
           p.Patient_Name, 
           d.Doctor_Name, 
           a.Appointment_Date, 
           a.Appointment_Time, 
           a.Appointment_Status
    FROM Appointment a
    JOIN Patient p ON a.Patient_ID = p.Patient_ID
    JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID;
END;
GO

-- Procedure to Update an Existing Appointment
CREATE PROCEDURE spUpdateAppointment
    @Appointment_ID INT,            -- Appointment ID to Identify the Record
    @Patient_ID INT,                -- Updated Patient ID
    @Doctor_ID INT,                 -- Updated Doctor ID
    @Appointment_Date DATE,         -- Updated Appointment Date
    @Appointment_Time TIME,         -- Updated Appointment Time
    @Appointment_Status NVARCHAR(20) -- Updated Appointment Status
AS
BEGIN
    UPDATE Appointment
    SET Patient_ID = @Patient_ID,
        Doctor_ID = @Doctor_ID,
        Appointment_Date = @Appointment_Date,
        Appointment_Time = @Appointment_Time,
        Appointment_Status = @Appointment_Status
    WHERE Appointment_ID = @Appointment_ID;
END;
GO

-- Procedure to Delete an Appointment
CREATE PROCEDURE spDeleteAppointment
    @Appointment_ID INT  -- Appointment ID to Identify the Record to be Deleted
AS
BEGIN
    DELETE FROM Appointment
    WHERE Appointment_ID = @Appointment_ID;
END;
GO

-- ===========================
-- Consultation Room Stored Procedures
-- ===========================

-- Procedure to Insert a New Consultation Room
CREATE PROCEDURE spInsertConsultationRoom
    @Appointment_ID INT,            -- Appointment ID Associated with the Consultation
    @Platform NVARCHAR(50),         -- Platform Used for the Consultation (e.g., Zoom, MS Teams)
    @Room_Status NVARCHAR(50),      -- Room Status (e.g., Available, In session)
    @Access_Code NVARCHAR(20),      -- Access Code for the Consultation Room
    @Start_Time TIME,               -- Consultation Start Time
    @End_Time TIME                  -- Consultation End Time
AS
BEGIN
    INSERT INTO Consultation_Room (Appointment_ID, Platform, Room_Status, Access_Code, Start_Time, End_Time)
    VALUES (@Appointment_ID, @Platform, @Room_Status, @Access_Code, @Start_Time, @End_Time);
END;
GO

-- Procedure to Retrieve All Consultation Rooms
CREATE PROCEDURE spRetrieveConsultationRooms
AS
BEGIN
    SELECT Room_ID, Appointment_ID, Platform, Room_Status, Access_Code, Start_Time, End_Time
    FROM Consultation_Room;
END;
GO

-- Procedure to Update an Existing Consultation Room
CREATE PROCEDURE spUpdateConsultationRoom
    @Room_ID INT,                   -- Room ID to Identify the Record
    @Appointment_ID INT,            -- Updated Appointment ID
    @Platform NVARCHAR(50),         -- Updated Platform
    @Room_Status NVARCHAR(50),      -- Updated Room Status
    @Access_Code NVARCHAR(20),      -- Updated Access Code
    @Start_Time TIME,               -- Updated Start Time
    @End_Time TIME                  -- Updated End Time
AS
BEGIN
    UPDATE Consultation_Room
    SET Appointment_ID = @Appointment_ID,
        Platform = @Platform,
        Room_Status = @Room_Status,
        Access_Code = @Access_Code,
        Start_Time = @Start_Time,
        End_Time = @End_Time
    WHERE Room_ID = @Room_ID;
END;
GO

-- Procedure to Delete a Consultation Room
CREATE PROCEDURE spDeleteConsultationRoom
    @Room_ID INT  -- Room ID to Identify the Record to be Deleted
AS
BEGIN
    DELETE FROM Consultation_Room
    WHERE Room_ID = @Room_ID;
END;
GO
