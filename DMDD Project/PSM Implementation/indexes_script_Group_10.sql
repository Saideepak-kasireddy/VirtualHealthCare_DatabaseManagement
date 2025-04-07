--Using the database
USE [Virtual_Healthcare]
GO


DROP INDEX IF EXISTS IX_Patient_Contact_Number ON Patient
CREATE NONCLUSTERED INDEX IX_Patient_Contact_Number 
ON Patient (Patient_Contact_Number);

DROP INDEX IF EXISTS IX_Patient_Name ON Patient
CREATE NONCLUSTERED INDEX IX_Patient_Name 
ON Patient (Patient_Name);

--The comment below tests the above indexing
--EXEC sp_helpindex 'Patient';


DROP INDEX IF EXISTS IX_Shipment_Bill_DeliveryDate ON Shipment
CREATE NONCLUSTERED INDEX IX_Shipment_Bill_DeliveryDate 
ON Shipment (Bill_ID, Expected_Delivery_Date);

--The comment below tests the above indexing
--EXEC sp_helpindex 'Shipment';

DROP INDEX IF EXISTS IX_Medication_Name ON Medication
CREATE NONCLUSTERED INDEX IX_Medication_Name 
ON Medication (Medication_Name);

--The comment below tests the above indexing
--EXEC sp_helpindex 'Medication';