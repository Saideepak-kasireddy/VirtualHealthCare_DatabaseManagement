-- iF DATABASE EXISTS, DROP
IF EXISTS (SELECT name FROM sys.databases WHERE name = N'Virtual_Healthcare')
    DROP DATABASE Virtual_Healthcare
GO

--Creating the Database
CREATE DATABASE [Virtual_Healthcare]
GO

--Using the database
USE [Virtual_Healthcare]
GO

-- Drop tables if they exist
DROP TABLE IF EXISTS Feedback, Payment, Shipment, Prescription_Detail, Medication, Bill, Prescription, Consultation_Room, Appointment, Medical_Record, Patient, Doctor, Department;

-- Create Department Table
CREATE TABLE Department (
    Department_ID INT IDENTITY(1,1) PRIMARY KEY,
    Department_Name VARCHAR(50) NOT NULL
);

-- Create Doctor Table
CREATE TABLE Doctor (
    Doctor_ID INT IDENTITY(1,1) PRIMARY KEY,
    Department_ID INT NOT NULL,
    Doctor_Name VARCHAR(100) NOT NULL,
    Doctor_Contact VARCHAR(15) NOT NULL,
    Doctor_Email VARCHAR(100) NOT NULL UNIQUE,
    Doctor_User_ID VARCHAR(50) NOT NULL UNIQUE,
    Doctor_Password VARCHAR(100) NOT NULL,
    Doctor_Specialty VARCHAR(50),
    Doctor_Availability VARCHAR(50) NOT NULL,
    FOREIGN KEY (Department_ID) REFERENCES Department(Department_ID)
);


-- Create Patient Table
CREATE TABLE Patient (
    Patient_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_Name VARCHAR(100) NOT NULL,
    Patient_DOB DATE NOT NULL,
    Patient_Contact_Number VARCHAR(15) NOT NULL,
    Patient_Email VARCHAR(100) NOT NULL UNIQUE,
    Patient_User_ID VARCHAR(50) NOT NULL UNIQUE,
    Patient_Password VARCHAR(100) NOT NULL,
    Insurance_ID VARCHAR(50),
    Patient_Address VARCHAR(255) NOT NULL,
);

-- Create Appointment Table
CREATE TABLE Appointment (
    Appointment_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_ID INT NOT NULL,
    Doctor_ID INT NOT NULL,
    Appointment_Date DATE NOT NULL,
    Appointment_Time TIME NOT NULL,
    Appointment_Status VARCHAR(20) CHECK (Appointment_Status IN ('Scheduled', 'Cancelled')),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);


-- Create Consultation Room Table
CREATE TABLE Consultation_Room (
    Room_ID INT IDENTITY(1,1) PRIMARY KEY,
    Appointment_ID INT NOT NULL,
    Platform VARCHAR(50) NOT NULL,
    Room_Status VARCHAR(50) NOT NULL CHECK (Room_Status IN ('Available', 'In session')),
    Access_Code VARCHAR(20),
    Start_Time TIME,
    End_Time TIME,
    FOREIGN KEY (Appointment_ID) REFERENCES Appointment(Appointment_ID)
);


-- Creating Medical Record Entity
CREATE TABLE Medical_Record (
    Record_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_ID INT NOT NULL,
    Blood_Type CHAR(3) CHECK (Blood_Type IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')),
    Diagnosis VARCHAR(255) NOT NULL,
    Treatment_Plan VARCHAR(255),
    Date DATE NOT NULL,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

-- Creating Prescription Entity
CREATE TABLE Prescription (
    Prescription_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_ID INT NOT NULL,
    Doctor_ID INT NOT NULL,
    Issue_Date DATE NOT NULL,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);

-- Create Medication Entity
CREATE TABLE Medication (
    Medication_ID INT IDENTITY(1,1) PRIMARY KEY,
    Medication_Name VARCHAR(100) NOT NULL,
    Medication_Cost DECIMAL(7,2) NOT NULL CHECK (Medication_Cost > 0),
    [Description] VARCHAR(255),
    Quantity_Instock INT NOT NULL CHECK (Quantity_Instock >= 0)
);

-- Create Prescription Detail Table
CREATE TABLE Prescription_Detail (
    Prescription_ID INT NOT NULL,
    Medication_ID INT NOT NULL,
    Usage_Instruction VARCHAR(255) NOT NULL,
    Quantity_Ordered INT CHECK (Quantity_Ordered > 0),
    Amount DECIMAL(10,2) CHECK (Amount >= 0),
    PRIMARY KEY (Prescription_ID, Medication_ID),
    FOREIGN KEY (Prescription_ID) REFERENCES Prescription(Prescription_ID),
    FOREIGN KEY (Medication_ID) REFERENCES Medication(Medication_ID)
);


-- Creating Bill Table
CREATE TABLE Bill (
    Bill_ID INT IDENTITY(1,1) PRIMARY KEY,
    Prescription_ID INT NOT NULL,
    IssueDate DATE NOT NULL,
    TotalAmount DECIMAL(10,2) CHECK (TotalAmount > 0),
    Status VARCHAR(20) CHECK (Status IN ('Paid', 'Unpaid')),
    FOREIGN KEY (Prescription_ID) REFERENCES Prescription(Prescription_ID)
);

-- Create Payment Table
CREATE TABLE Payment (
    Payment_ID INT IDENTITY(1,1) PRIMARY KEY,
    Bill_ID INT NOT NULL,
    AmountPaid DECIMAL(10,2) NOT NULL CHECK (AmountPaid >= 0),
    PaymentDate DATE NOT NULL,
    PaymentMethod VARCHAR(50),
    FOREIGN KEY (Bill_ID) REFERENCES Bill(Bill_ID)
);

-- Create Shipment Table
CREATE TABLE Shipment (
    Shipment_ID INT IDENTITY(1,1) PRIMARY KEY,
    Bill_ID INT NOT NULL,
    Patient_ID INT NOT NULL,
    Shipment_Address VARCHAR(255) NOT NULL,
    Delivery_Status VARCHAR(50) CHECK (Delivery_Status IN ('Shipped', 'In Transit', 'Delivered')),
    Tracking_Number VARCHAR(50),
    Expected_Delivery_Date DATE,
    Delivery_Date DATE,
    FOREIGN KEY (Bill_ID) REFERENCES Bill(Bill_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

-- Create Feedback Table
CREATE TABLE Feedback (
    Feedback_ID INT IDENTITY(1,1) PRIMARY KEY,
    Patient_ID INT NOT NULL,
    Appointment_ID INT NOT NULL,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Comments VARCHAR(255),
    Feedback_Date DATE NOT NULL,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Appointment_ID) REFERENCES Appointment(Appointment_ID)
);


