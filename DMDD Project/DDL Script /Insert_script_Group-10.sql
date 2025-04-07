USE Virtual_Healthcare
GO

INSERT INTO Department (Department_Name)
VALUES 
('Cardiology'),
('Neurology'),
('Orthopedics'),
('Dermatology'),
('Pediatrics'),
('General Medicine'),
('Gynecology'),
('Ophthalmology'),
('Dentistry'),
('Urology'),
('Endocrinology'),
('Psychiatry'),
('Rheumatology'),
('Gastroenterology'),
('Pulmonology');

PRINT 'The Department Table';
SELECT * from Department;

 
INSERT INTO Doctor (Department_ID, Doctor_Name, Doctor_Contact, Doctor_Email, Doctor_User_ID, Doctor_Password, Doctor_Specialty, Doctor_Availability)
VALUES
(1, 'Dr. Ethan Heartfield', '6789012345', 'ethan.heartfield@healthcare.com', 'ethan_h', 'HeartField#123', 'Cardiologist', 'Monday to Friday 10 AM - 6 PM'),
(2, 'Dr. Sophia Branfield', '7890123456', 'sophia.branfield@healthcare.com', 'sophia_b', 'BrainPro!456', 'Neurologist', 'Wednesday to Sunday 9 AM - 3 PM'),
(3, 'Dr. Olivia Skinner', '8901234567', 'olivia.skinner@healthcare.com', 'olivia_s', 'SkinCare789$', 'Dermatologist', 'Tuesday to Friday 8 AM - 4 PM'),
(4, 'Dr. Liam Strongwell', '9012345678', 'liam.strongwell@healthcare.com', 'liam_s', 'StrongWell#654', 'Orthopedic Surgeon', 'Monday to Thursday 9 AM - 5 PM'),
(5, 'Dr. Amelia Childman', '1122334455', 'amelia.childman@healthcare.com', 'amelia_c', 'ChildCare@123', 'Pediatrician', 'Tuesday to Saturday 8 AM - 4 PM'),
(6, 'Dr. Noah Goodman', '2233445566', 'noah.goodman@healthcare.com', 'noah_g', 'GoodPass$456', 'General Physician', 'Monday to Friday 9 AM - 3 PM'),
(7, 'Dr. Mia Clearwater', '3344556677', 'mia.clearwater@healthcare.com', 'mia_c', 'ClearVision@789', 'Ophthalmologist', 'Monday to Saturday 10 AM - 5 PM'),
(8, 'Dr. Lucas Brightwell', '4455667788', 'lucas.brightwell@healthcare.com', 'lucas_b', 'BrightSmile$321', 'Dentist', 'Monday to Friday 9 AM - 5 PM'),
(9, 'Dr. Grace Jointly', '5566778899', 'grace.jointly@healthcare.com', 'grace_j', 'JointCare#456', 'Rheumatologist', 'Tuesday to Saturday 8 AM - 4 PM'),
(10, 'Dr. Henry Earstone', '6677889900', 'henry.earstone@healthcare.com', 'henry_e', 'EarSpecial!123', 'ENT Specialist', 'Wednesday to Sunday 10 AM - 6 PM'),
(11, 'Dr. Ella Mindwell', '7788990011', 'ella.mindwell@healthcare.com', 'ella_m', 'MindCare@789', 'Psychiatrist', 'Monday to Friday 9 AM - 4 PM'),
(12, 'Dr. James Heartstrong', '8899001122', 'james.heartstrong@healthcare.com', 'james_h', 'HeartPro#321', 'Cardiologist', 'Monday to Thursday 8 AM - 2 PM'),
(13, 'Dr. Lily Nerveline', '9900112233', 'lily.nerveline@healthcare.com', 'lily_n', 'NerveLine@456', 'Neurologist', 'Tuesday to Saturday 9 AM - 3 PM'),
(14, 'Dr. Benjamin Flexfield', '1112223344', 'benjamin.flexfield@healthcare.com', 'benjamin_f', 'FlexStrong#789', 'Physiotherapist', 'Monday to Friday 10 AM - 5 PM'),
(15, 'Dr. Chloe Healwell', '2223334455', 'chloe.healwell@healthcare.com', 'chloe_h', 'HealExpert@123', 'General Physician', 'Monday to Saturday 8 AM - 6 PM');

SELECT * from Doctor;

INSERT INTO Patient (Patient_Name, Patient_DOB, Patient_Contact_Number, Patient_Email, Patient_User_ID, Patient_Password, Insurance_ID, Patient_Address)
VALUES
('John Doe', '1980-05-15', '1112223333', 'john.doe@gmail.com', 'john_d', 'JohnSecure1', 'INS123', '123 Maple Street, Cityville'),
('Jane Smith', '1992-07-20', '2223334444', 'jane.smith@gmail.com', 'jane_s', 'JaneSafe2', 'INS456', '456 Oak Avenue, Townsville'),
('Mike Johnson', '1985-09-12', '3334445555', 'mike.johnson@gmail.com', 'mike_j', 'MikeSecure3', 'INS789', '789 Pine Road, Villagetown'),
('Emily Davis', '1990-03-25', '4445556666', 'emily.davis@gmail.com', 'emily_d', 'EmilySafe4', 'INS321', '321 Elm Lane, Suburbia'),
('Sarah Wilson', '2000-12-30', '5556667777', 'sarah.wilson@gmail.com', 'sarah_w', 'SarahSecure5', 'INS654', '654 Birch Blvd, Uptown'),
('Robert Brown', '1987-11-08', '6667778888', 'robert.brown@gmail.com', 'robert_b', 'RobertSecure6', 'INS987', '987 Cedar Way, Cityscape'),
('Linda Green', '1995-01-14', '7778889999', 'linda.green@gmail.com', 'linda_g', 'LindaSafe7', 'INS852', '852 Maple Avenue, Greentown'),
('James White', '1983-06-22', '8889990000', 'james.white@gmail.com', 'james_w', 'JamesSecure8', 'INS741', '741 Willow Street, Harmony'),
('Patricia Black', '1998-04-03', '9990001111', 'patricia.black@gmail.com', 'patricia_b', 'PatriciaSafe9', 'INS369', '369 Poplar Drive, Suburbia'),
('Michael Taylor', '1990-08-18', '0001112222', 'michael.taylor@gmail.com', 'michael_t', 'MichaelSecure10', 'INS159', '159 Chestnut Boulevard, Uptown'),
('Barbara Harris', '1982-02-25', '1112223334', 'barbara.harris@gmail.com', 'barbara_h', 'BarbaraSafe11', 'INS753', '753 Spruce Circle, Metropolis'),
('William Adams', '1996-09-30', '2223334445', 'william.adams@gmail.com', 'william_a', 'WilliamSecure12', 'INS654', '654 Walnut Crescent, Hilltown'),
('Elizabeth Clark', '2001-12-05', '3334445556', 'elizabeth.clark@gmail.com', 'elizabeth_c', 'ElizabethSafe13', 'INS321', '321 Sycamore Lane, Downtown'),
('David Lewis', '1979-07-11', '4445556667', 'david.lewis@gmail.com', 'david_l', 'DavidSecure14', 'INS852', '852 Fir Road, Lakeside'),
('Susan Hall', '1993-10-29', '5556667778', 'susan.hall@gmail.com', 'susan_h', 'SusanSafe15', 'INS963', '963 Redwood Path, Countryside');

SELECT * FROM Patient;

INSERT INTO Appointment (Patient_ID, Doctor_ID, Appointment_Date, Appointment_Time, Appointment_Status) VALUES
(1, 1, '2024-11-10', '09:30:00', 'Scheduled'),
(2, 2, '2024-11-11', '13:00:00', 'Scheduled'),
(3, 3, '2024-11-12', '14:30:00', 'Cancelled'),
(4, 4, '2024-11-13', '08:00:00', 'Scheduled'),
(5, 5, '2024-11-14', '09:00:00', 'Scheduled'),
(6, 6, '2024-11-15', '13:15:00', 'Scheduled'),
(7, 7, '2024-11-16', '09:45:00', 'Scheduled'),
(8, 8, '2024-11-17', '14:00:00', 'Cancelled'),
(9, 9, '2024-11-18', '15:30:00', 'Scheduled'),
(10, 10, '2024-11-19', '08:15:00', 'Scheduled'),
(11, 11, '2024-11-20', '09:15:00', 'Scheduled'),
(12, 12, '2024-11-21', '13:30:00', 'Scheduled'),
(13, 13, '2024-11-22', '10:00:00', 'Scheduled'),
(14, 14, '2024-11-23', '14:30:00', 'Cancelled'),
(15, 15, '2024-11-24', '09:00:00', 'Scheduled');

SELECT * from Appointment;

INSERT INTO Consultation_Room (Appointment_ID, Platform, Room_Status, Access_Code, Start_Time, End_Time) VALUES
(1, 'Zoom', 'Available', 'ABC123', '09:30:00', '10:30:00'),
(2, 'Teams', 'In session', 'DEF456', '13:00:00', '14:00:00'),
(3, 'Google Meet', 'Available', 'GHI789', '14:30:00', '15:30:00'),
(4, 'Zoom', 'In session', 'JKL012', '08:00:00', '09:00:00'),
(5, 'Teams', 'Available', 'MNO345', '09:00:00', '10:00:00'),
(6, 'Google Meet', 'In session', 'PQR678', '13:15:00', '14:15:00'),
(7, 'Zoom', 'Available', 'STU901', '09:45:00', '10:45:00'),
(8, 'Teams', 'In session', 'VWX234', '14:00:00', '15:00:00'),
(9, 'Google Meet', 'Available', 'YZA567', '15:30:00', '16:30:00'),
(10, 'Zoom', 'In session', 'BCD890', '08:15:00', '09:15:00'),
(11, 'Teams', 'Available', 'EFG123', '09:15:00', '10:15:00'),
(12, 'Google Meet', 'In session', 'HIJ456', '13:30:00', '14:30:00'),
(13, 'Zoom', 'Available', 'KLM789', '10:00:00', '11:00:00'),
(14, 'Teams', 'In session', 'NOP012', '14:30:00', '15:30:00'),
(15, 'Google Meet', 'Available', 'QRS345', '09:00:00', '10:00:00');

SELECT * FROM Consultation_Room;

INSERT INTO Medical_Record (Patient_ID, Blood_Type, Diagnosis, Treatment_Plan, Date)
VALUES
(1, 'A+', 'Hypertension', 'Lifestyle changes, Medication', '2024-11-12'),
(2, 'B-', 'Migraine', 'Pain relief, Rest', '2024-11-13'),
(3, 'O+', 'Fracture', 'Cast, Pain relief', '2024-11-14'),
(4, 'AB-', 'Eczema', 'Topical creams', '2024-11-15'),
(5, 'A-', 'Viral Infection', 'Rest, Fluids', '2024-11-16'),
(6, 'O-', 'Diabetes', 'Insulin, Diet control', '2024-11-17'),
(7, 'B+', 'Pregnancy', 'Prenatal vitamins', '2024-11-18'),
(8, 'AB+', 'Eye Infection', 'Antibiotics', '2024-11-19'),
(9, 'O+', 'Tooth Decay', 'Filling, Cleaning', '2024-11-20'),
(10, 'A+', 'Urinary Tract Infection', 'Antibiotics', '2024-11-21'),
(11, 'B-', 'Thyroid Disorder', 'Thyroid medication', '2024-11-22'),
(12, 'O-', 'Anxiety', 'Therapy, Medication', '2024-11-23'),
(13, 'A+', 'Arthritis', 'Pain relief, Exercise', '2024-11-24'),
(14, 'AB+', 'Indigestion', 'Antacids, Diet changes', '2024-11-25'),
(15, 'B-', 'Asthma', 'Inhaler, Avoid triggers', '2024-11-26');

SELECT * FROM Medical_Record;

INSERT INTO Prescription (Patient_ID, Doctor_ID, Issue_Date)
VALUES
(1, 1, '2024-11-12'),
(2, 2, '2024-11-13'),
(3, 3, '2024-11-14'),
(4, 4, '2024-11-15'),
(5, 5, '2024-11-16'),
(6, 6, '2024-11-17'),
(7, 7, '2024-11-18'),
(8, 8, '2024-11-19'),
(9, 9, '2024-11-20'),
(10, 10, '2024-11-21'),
(11, 11, '2024-11-22'),
(12, 12, '2024-11-23'),
(13, 13, '2024-11-24'),
(14, 14, '2024-11-25'),
(15, 15, '2024-11-26');

SELECT * FROM Prescription;

INSERT INTO Medication (Medication_Name, Medication_Cost, [Description], Quantity_Instock)
VALUES
('Aspirin', 10.50, 'Pain relief', 100),
('Paracetamol', 8.30, 'Pain relief', 150),
('Amoxicillin', 12.75, 'Antibiotic', 200),
('Ibuprofen', 15.60, 'Pain relief', 120),
('Metformin', 25.40, 'Diabetes medication', 180),
('Simvastatin', 20.00, 'Cholesterol medication', 130),
('Insulin', 50.00, 'Diabetes medication', 60),
('Antihistamine', 5.50, 'Allergy relief', 250),
('Vitamin C', 7.20, 'Supplement', 300),
('Antacid', 4.30, 'Stomach relief', 220),
('Cough Syrup', 11.00, 'Cough relief', 90),
('Eyelid Cream', 13.50, 'For eye infections', 75),
('Atenolol', 18.40, 'Blood pressure medication', 140),
('Naproxen', 14.60, 'Pain relief', 160),
('Steroid Cream', 22.00, 'For skin issues', 110);

SELECT * FROM Medication;

INSERT INTO Prescription_Detail (Prescription_ID, Medication_ID, Usage_Instruction, Quantity_Ordered)
VALUES
(1, 1, 'Take one tablet every 6 hours', 10),
(1, 2, 'Take one tablet every 12 hours', 10),
(1, 3, 'Take one tablet three times a day', 12),
(2, 2, 'Take one tablet every 4 hours', 30),
(2, 1, 'Take one tablet every 6 hours', 28),
(2, 6, 'Take one tablet daily', 28),
(3, 3, 'Take one tablet three times a day', 50),
(3, 5, 'Take one tablet twice a day', 40),
(4, 4, 'Take two tablets every 8 hours', 40),
(4, 7, 'Take two tablets every 6 hours', 42),
(5, 9, 'Take one tablet with meals', 60),
(5, 10, 'Take one tablet with breakfast', 55),
(5, 7, 'Take one tablet with meals', 60),
(6, 12, 'Take one tablet daily', 70),
(6, 3, 'Take one tablet every night', 65),
(7, 6, 'Inject daily', 30),
(7, 14, 'Inject twice daily', 35),
(8, 15, 'Take one tablet before bed', 50),
(8, 11, 'Take one tablet before dinner', 48),
(9, 10, 'Take one tablet as needed', 40),
(9, 12, 'Take two tablets as needed', 45),
(10, 11, 'Take one tablet twice a day', 50),
(10, 14, 'Take one tablet thrice a day', 55),
(11, 15, 'Take one tablet daily', 30),
(11, 1, 'Take one tablet every night', 28),
(12, 4, 'Take one tablet every morning', 25),
(12, 2, 'Take one tablet every afternoon', 20),
(13, 11, 'Apply to affected area twice a day', 10),
(13, 12, 'Apply to affected area three times a day', 12),
(14, 6, 'Take one tablet every morning', 20),
(14, 9, 'Take one tablet every night', 18),
(15, 7, 'Apply to skin twice a day', 15),
(15, 15, 'Apply to skin three times a day', 17);

SELECT * FROM Prescription_Detail;

SELECT * FROM Bill;

INSERT INTO Payment (Bill_ID, AmountPaid, PaymentDate, PaymentMethod)
VALUES
(1, 420.00, '2024-11-12', 'Credit Card'),
(2, 249.00, '2024-11-13', 'Credit Card'),
(3, 2050.00, '2024-11-14', 'Debit Card'),
(4, 624.00, '2024-11-15', 'Credit Card'),
(5, 816.00, '2024-11-16', 'Debit Card'),
(6, 1800.00, '2024-11-17', 'Debit Card'),
(7, 3000.00, '2024-11-18', 'Credit Card'),
(8, 550.00, '2024-11-19', 'Debit Card'),
(9, 172.00, '2024-11-20', 'Debit Card'),
(10, 360.00, '2024-11-21', 'Credit Card'),
(11, 546.00, '2024-11-22', 'Credit Card'),
(12, 260.00, '2024-11-23', 'Debit Card'),
(13, 405.00, '2024-11-24', 'Debit Card'),
(14, 288.00, '2024-11-25', 'Credit Card'),
(15, 660.00, '2024-11-26', 'Credit Card');

SELECT * FROM Payment;

INSERT INTO Shipment (Bill_ID, Patient_ID, Shipment_Address, Delivery_Status, Tracking_Number, Expected_Delivery_Date, Delivery_Date)
VALUES
(1, 1, '123 Elm St, Cityville', 'Shipped', 'TRK001', '2024-11-14', '2024-11-14'),
(2, 2, '456 Oak St, Townsville', 'Shipped', 'TRK002', '2024-11-15', '2024-11-15'),
(3, 3, '789 Pine St, Smalltown', 'In Transit', 'TRK003', '2024-11-16', NULL),
(4, 4, '321 Maple St, Villagetown', 'Delivered', 'TRK004', '2024-11-17', '2024-11-16'),
(5, 5, '654 Birch St, Suburbia', 'In Transit', 'TRK005', '2024-11-18', NULL),
(6, 6, '987 Cedar St, Bigcity', 'Delivered', 'TRK006', '2024-11-19', '2024-11-19'),
(7, 7, '112 Willow St, Riverside', 'Shipped', 'TRK007', '2024-11-20', '2024-11-20'),
(8, 8, '223 Fir St, Greenfield', 'Delivered', 'TRK008', '2024-11-21', '2024-11-21'),
(9, 9, '334 Spruce St, Lakeview', 'In Transit', 'TRK009', '2024-11-22', NULL),
(10, 10, '445 Cedar St, Highland Park', 'Shipped', 'TRK010', '2024-11-23', '2024-11-23'),
(11, 11, '556 Pine St, Mountainview', 'Delivered', 'TRK011', '2024-11-24', '2024-11-24'),
(12, 12, '667 Oak St, Foresttown', 'Shipped', 'TRK012', '2024-11-25', '2024-11-25'),
(13, 13, '778 Birch St, Hilltop', 'In Transit', 'TRK013', '2024-11-26', NULL),
(14, 14, '889 Maple St, Uptown', 'Delivered', 'TRK014', '2024-11-27', '2024-11-27'),
(15, 15, '990 Cedar St, Downtown', 'Shipped', 'TRK015', '2024-11-28', '2024-11-28');

SELECT * FROM Shipment;


INSERT INTO Feedback (Patient_ID, Appointment_ID, Rating, Comments, Feedback_Date) VALUES
(3, 5, 5, 'Excellent service and very attentive staff.', '2024-11-10'),
(7, 9, 4, 'Great service but some delays.', '2024-11-11'),
(1, 2, 3, 'Fair service, staff could be more organized.', '2024-11-11'),
(14, 13, 5, 'Very satisfied with the care received.', '2024-11-12'),
(8, 6, 4, 'Doctor was knowledgeable but a bit rushed.', '2024-11-12'),
(15, 3, 2, 'Booking process was difficult and frustrating.', '2024-11-13'),
(10, 12, 3, 'Room for improvement in the waiting area.', '2024-11-14'),
(6, 10, 5, 'Amazing experience, doctor was very kind.', '2024-11-15'),
(2, 15, 4, 'Service was great, but facilities need improvement.', '2024-11-15'),
(12, 11, 3, 'Okay service but staff could be more attentive.', '2024-11-16'),
(9, 7, 5, 'Perfect, very compassionate staff.', '2024-11-16'),
(4, 14, 1, 'Unhappy with consultation, felt rushed.', '2024-11-17'),
(11, 8, 2, 'Long wait times and average service.', '2024-11-17'),
(13, 4, 5, 'Fantastic experience, felt very cared for.', '2024-11-18'),
(5, 1, 3, 'Average experience, room for improvement.', '2024-11-19'),
(3, 9, 4, 'Helpful staff and smooth booking process.', '2024-11-19'),
(14, 13, 5, 'Doctor provided excellent guidance.', '2024-11-20'),
(8, 2, 2, 'Difficult to find appointment slots.', '2024-11-20'),
(15, 6, 4, 'Overall good service but some delays.', '2024-11-21'),
(1, 3, 5, 'Extremely satisfied with the service.', '2024-11-22'),
(12, 11, 3, 'Decent experience, but consultation was brief.', '2024-11-22'),
(6, 7, 5, 'Very attentive and caring staff.', '2024-11-23'),
(10, 15, 4, 'Efficient and helpful service.', '2024-11-23'),
(9, 14, 2, 'Unhappy with the booking process.', '2024-11-24'),
(4, 8, 3, 'Satisfactory service, could improve facilities.', '2024-11-24'),
(13, 4, 5, 'Excellent consultation and care.', '2024-11-25'),
(7, 12, 5, 'Fantastic experience, no complaints.', '2024-11-25'),
(2, 10, 4, 'Doctor was very professional.', '2024-11-26'),
(11, 1, 2, 'Service quality has decreased.', '2024-11-26'),
(5, 5, 3, 'Decent experience, but needs improvement.', '2024-11-27'),
(8, 9, 5, 'Amazing staff and service!', '2024-11-28'),
(15, 3, 4, 'Good experience overall, no major issues.', '2024-11-29'),
(14, 6, 3, 'Satisfactory but not exceptional.', '2024-11-30'),
(12, 13, 5, 'Highly recommend this clinic.', '2024-12-01');

SELECT * FROM Feedback;






