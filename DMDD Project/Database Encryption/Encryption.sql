--Encryption File

USE Virtual_Healthcare;
GO

CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'StrongMasterKey@2024!';
GO

CREATE CERTIFICATE VirtualHC_Cert
WITH SUBJECT = 'Virtual Healthcare Encryption Certificate';
GO

CREATE SYMMETRIC KEY VirtualHC_Key
WITH ALGORITHM = AES_256
ENCRYPTION BY CERTIFICATE VirtualHC_Cert;
GO

--ALTER TABLE Patient
--ADD Encrypted_Password VARBINARY(MAX);
--GO

OPEN SYMMETRIC KEY VirtualHC_Key
DECRYPTION BY CERTIFICATE VirtualHC_Cert;

UPDATE Patient
SET Patient_Password = ENCRYPTBYKEY(KEY_GUID('VirtualHC_Key'), CONVERT(VARBINARY, Patient_Password));

CLOSE SYMMETRIC KEY VirtualHC_Key;


GO
DROP TRIGGER IF EXISTS trg_EncryptPassword
GO
CREATE TRIGGER trg_EncryptPassword
ON Patient
AFTER INSERT, UPDATE
AS
BEGIN
    OPEN SYMMETRIC KEY VirtualHC_Key
    DECRYPTION BY CERTIFICATE VirtualHC_Cert;

    -- Encrypt newly inserted or updated passwords
    UPDATE Patient
    SET Patient_Password = ENCRYPTBYKEY(KEY_GUID('VirtualHC_Key'), CONVERT(VARBINARY, Patient_Password))
    WHERE Patient_ID IN (SELECT Patient_ID FROM inserted);

    CLOSE SYMMETRIC KEY VirtualHC_Key;
END;
GO



INSERT INTO Patient (Patient_Name, Patient_DOB, Patient_Contact_Number, Patient_Email, Patient_User_ID, Patient_Password, Insurance_ID, Patient_Address)
VALUES 
('Deepak Doe', '1990-01-01', '1234567890', 'deepak.doe@example.com', 'john_doe', 'SecurePassword123', 'INS001', '123 Main Street');

SELECT * FROM Patient;

--Decrypt

--Open Symmetric Key
OPEN SYMMETRIC KEY VirtualHC_Key
DECRYPTION BY CERTIFICATE VirtualHC_Cert;


--Retrieve Decrypted Data
SELECT 
    Patient_ID,
    Patient_Name,
    CONVERT(VARCHAR, DECRYPTBYKEY(Patient_Password)) AS Decrypted_Password
FROM Patient;

CLOSE SYMMETRIC KEY VirtualHC_Key;
