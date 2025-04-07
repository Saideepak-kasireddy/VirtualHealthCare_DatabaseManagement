# 🏥 Virtual Healthcare Database Management System

## 📌 Overview  
This project is a comprehensive **Virtual Healthcare Database Management System** designed to streamline and optimize healthcare data operations. It provides a robust backend foundation for managing **patients, doctors, appointments, treatments, billing**, and more—ensuring secure, scalable, and efficient data handling in a virtual healthcare environment.

---

## 📐 Database Design  
The project began with the development of an **Entity-Relationship Diagram (ERD)** using **ER/Studio**, outlining the core structure of the virtual healthcare system. This included identifying and modeling essential entities such as:
- Patients  
- Doctors  
- Appointments  
- Medical Records  
- Treatments  
- Billing  
- Departments  

Special attention was given to the **relationships and cardinalities** to ensure a **scalable and normalized schema**.

---

## 🗄️ Database Implementation  
Using **SQL** and **SQL Server Management Studio (SSMS)**, the database was implemented based on the ERD. Key highlights include:
- Creation of tables with appropriate **primary and foreign key constraints**  
- Enforcement of **business rules** via check constraints, default values, and precise data types  
- Establishment of referential integrity across all healthcare modules  

---

## ⚙️ Functionalities Implementation  
To support system operations, a variety of database functionalities were implemented:
- **Stored Procedures** for scheduling appointments and generating billing summaries  
- **User-Defined Functions** to calculate outstanding balances and patient visit histories  
- **Triggers** to auto-update appointment statuses and billing process  
- **Views** for simplified access to aggregated patient care and doctor schedules  
- **Indexes** to improve performance on high-frequency queries  

---

## 📊 Integration with PowerBI  
For real-time healthcare insights, the SSMS database was integrated with **PowerBI** to build **interactive dashboards**. These dashboards help monitor:
- Patient visits by department  
- Doctor utilization rates  
- Billing trends  
- Treatment outcomes  

These visualizations empower healthcare administrators and staff to make **data-driven decisions**.

---


## 🛠️ Tools Used
- SQL  
- SQL Server Management Studio (SSMS)  
- ER/Studio  
- Tableau  

---

### 🗂️ ER Diagram (Logical View)
![Image](https://github.com/user-attachments/assets/f51e32e9-a990-4f10-82f3-d686045dd3da)

