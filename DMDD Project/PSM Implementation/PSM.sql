--Using the database
USE [Virtual_Healthcare]
GO

--Triggers

--1) Trigger to Calculate the Amount in the Prescription_Detail Table

GO
DROP TRIGGER IF EXISTS trg_CalculateAmount
GO
CREATE TRIGGER trg_CalculateAmount
ON Prescription_Detail
AFTER INSERT, UPDATE
AS
BEGIN
    UPDATE Prescription_Detail
    SET Amount = i.Quantity_Ordered * m.Medication_Cost
    FROM Prescription_Detail pd
    JOIN inserted i ON pd.Prescription_ID = i.Prescription_ID AND pd.Medication_ID = i.Medication_ID
    JOIN Medication m ON m.Medication_ID = i.Medication_ID;
END;
GO


--2) Trigger to calculate the TotalAmount in the Bill Table

GO
DROP TRIGGER IF EXISTS trg_PrescriptionDetail_Bill_1
GO
CREATE TRIGGER trg_PrescriptionDetail_Bill_1
ON Prescription_Detail
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Temporary table to store total amounts for all affected Prescription_IDs
    DECLARE @Totals TABLE (
        Prescription_ID INT,
        TotalAmount DECIMAL(10, 2)
    );

    -- Insert totals into the temporary table
    INSERT INTO @Totals (Prescription_ID, TotalAmount)
    SELECT 
        Prescription_ID,
        SUM(Amount) AS TotalAmount
    FROM Prescription_Detail
    WHERE Prescription_ID IN (SELECT DISTINCT Prescription_ID FROM inserted)
    GROUP BY Prescription_ID;

    -- Update existing bills
    UPDATE Bill
    SET 
        TotalAmount = t.TotalAmount,
        IssueDate = GETDATE()
    FROM Bill b
    INNER JOIN @Totals t ON b.Prescription_ID = t.Prescription_ID;

    -- Insert new bills for prescriptions that do not already have a bill
    INSERT INTO Bill (Prescription_ID, IssueDate, TotalAmount, Status)
    SELECT 
        t.Prescription_ID,
        GETDATE(),
        t.TotalAmount,
        'Unpaid'
    FROM @Totals t
    WHERE NOT EXISTS (
        SELECT 1 
        FROM Bill b 
        WHERE b.Prescription_ID = t.Prescription_ID
    );
END;


--Creating Stored Procedures

--1) Getting the top Medications by Sales

DROP PROCEDURE IF EXISTS sp_GetTopMedicationsBySales;
GO

CREATE PROCEDURE sp_GetTopMedicationsBySales
    @TopN INT
AS
BEGIN
    SELECT TOP (@TopN)
        m.Medication_Name,
        SUM(pd.Quantity_Ordered) AS TotalQuantity,
        SUM(pd.Amount) AS TotalSales
    FROM Prescription_Detail pd
    JOIN Medication m ON pd.Medication_ID = m.Medication_ID
    GROUP BY m.Medication_Name
    ORDER BY TotalSales DESC;
END;
GO

--The comment below tests the above store procedure
--EXEC sp_GetTopMedicationsBySales @TopN = 3;

--2) Getting the Summary of the Bill

DROP PROCEDURE IF EXISTS sp_GetBillSummary;
GO
CREATE PROCEDURE sp_GetBillSummary
    @BillID INT
AS
BEGIN
    SELECT 
        b.Bill_ID,
        p.Patient_Name,
        pr.Issue_Date AS Prescription_Issue_Date,
        pd.Medication_ID,
        m.Medication_Name,
        pd.Quantity_Ordered,
        pd.Amount AS Medication_Amount,
        b.TotalAmount,
        b.Status
    FROM Bill b
    JOIN Prescription pr ON b.Prescription_ID = pr.Prescription_ID
    JOIN Patient p ON pr.Patient_ID = p.Patient_ID
    JOIN Prescription_Detail pd ON pr.Prescription_ID = pd.Prescription_ID
    JOIN Medication m ON pd.Medication_ID = m.Medication_ID
    WHERE b.Bill_ID = @BillID;
END;

--The comment below tests the above store procedure
--EXEC sp_GetBillSummary @BillID = 1;


-- 3) Stored Procedures to List Appointments for a Specific Date

DROP PROCEDURE IF EXISTS sp_GetAppointmentsByDate;
GO
CREATE PROCEDURE sp_GetAppointmentsByDate
    @AppointmentDate DATE
AS
BEGIN
    SELECT 
        a.Appointment_ID,
        p.Patient_Name,
        d.Doctor_Name,
        a.Appointment_Time,
        a.Appointment_Status
    FROM Appointment a
    JOIN Patient p ON a.Patient_ID = p.Patient_ID
    JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID
    WHERE a.Appointment_Date = @AppointmentDate;
END;

--The comment below tests the above store procedure
--EXEC sp_GetAppointmentsByDate @AppointmentDate = '2024-11-23';


-- Creating Views 

-- 1) View for patient appointment details

DROP VIEW IF EXISTS vw_PatientAppointments;
GO
CREATE VIEW vw_PatientAppointments AS
SELECT 
    p.Patient_Name,
    d.Doctor_Name,
    a.Appointment_Date,
    a.Appointment_Time,
    a.Appointment_Status
FROM Appointment a
JOIN Patient p ON a.Patient_ID = p.Patient_ID
JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID;
GO

--The comment below tests the above View
--SELECT * FROM vw_PatientAppointments;


-- 2) View to track medication usage and stock levels.
DROP VIEW IF EXISTS vw_MedicationUsageStock;
GO
CREATE VIEW vw_MedicationUsageStock AS
SELECT 
    m.Medication_ID,
    m.Medication_Name,
    m.Description,
    m.Quantity_Instock,
    ISNULL(SUM(pd.Quantity_Ordered), 0) AS Total_Ordered,
    (m.Quantity_Instock - ISNULL(SUM(pd.Quantity_Ordered), 0)) AS Available_Stock
FROM 
    Medication m
LEFT JOIN 
    Prescription_Detail pd ON m.Medication_ID = pd.Medication_ID
GROUP BY 
    m.Medication_ID, m.Medication_Name, m.Description, m.Quantity_Instock;
GO

--The comment below tests the above View
--SELECT * FROM vw_MedicationUsageStock;

-- 3) View for Detailed Prescription Information

DROP VIEW IF EXISTS vw_DetailedPrescriptions;
GO
CREATE VIEW vw_DetailedPrescriptions AS
SELECT 
    pr.Prescription_ID,
    p.Patient_Name,
    d.Doctor_Name,
    pr.Issue_Date,
    m.Medication_Name,
    pd.Quantity_Ordered,
    pd.Amount
FROM 
    Prescription pr
JOIN 
    Patient p ON pr.Patient_ID = p.Patient_ID
JOIN 
    Doctor d ON pr.Doctor_ID = d.Doctor_ID
JOIN 
    Prescription_Detail pd ON pr.Prescription_ID = pd.Prescription_ID
JOIN 
    Medication m ON pd.Medication_ID = m.Medication_ID;
GO

--The comment below tests the above View
--SELECT * FROM vw_DetailedPrescriptions;


-- Creating User Defined Functions

--1) Function to Calculate Age Based on DOB
DROP FUNCTION IF EXISTS fn_CalculateAge;
GO
CREATE FUNCTION fn_CalculateAge (@DOB DATE)
RETURNS INT
AS
BEGIN
    RETURN DATEDIFF(YEAR, @DOB, GETDATE()) - 
           CASE WHEN MONTH(@DOB) > MONTH(GETDATE()) OR 
                     (MONTH(@DOB) = MONTH(GETDATE()) AND DAY(@DOB) > DAY(GETDATE()))
                THEN 1 ELSE 0 END;
END;
GO

--The comment below tests the above User Defined Function
--SELECT Patient_Name, dbo.fn_CalculateAge(Patient_DOB) AS Age FROM Patient;


--2) Funtion to calculate Average Feedback Rating
DROP FUNCTION IF EXISTS fn_GetAverageFeedbackRating;
GO

CREATE FUNCTION fn_GetAverageFeedbackRating (@DoctorID INT)
RETURNS DECIMAL(3, 2)
AS
BEGIN
    RETURN (
        SELECT AVG(CAST(f.Rating AS DECIMAL(3, 2)))
        FROM Feedback f
        JOIN Appointment a ON f.Appointment_ID = a.Appointment_ID
        WHERE a.Doctor_ID = @DoctorID
    );
END;
GO

--The comment below tests the above User Defined Function

--Get the average feedback rating for a doctor with Doctor_ID = 1
--SELECT dbo.fn_GetAverageFeedbackRating(1) AS AverageRatingForDoctor;


-- 3) Function to Get Total Appointments for a Doctor
DROP FUNCTION IF EXISTS fn_GetTotalAppointmentsForDoctor;
GO
CREATE FUNCTION fn_GetTotalAppointmentsForDoctor (@DoctorID INT)
RETURNS INT
AS
BEGIN
    RETURN (
        SELECT COUNT(*)
        FROM Appointment
        WHERE Doctor_ID = @DoctorID
    );
END;
GO


--The comment below tests the above User Defined Function
--SELECT Doctor_Name, dbo.fn_GetTotalAppointmentsForDoctor(Doctor_ID) AS TotalAppointments
--FROM Doctor;




