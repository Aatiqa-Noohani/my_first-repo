Title: Employee Management System
made by: Aatiqa Noohani 


Project Overview:
A Python-based GUI application to manage employees, using OOP concepts and file handling.
Allows Add, Update, Delete, Search by ID, Refresh, and Show Full Info of employees.


The project demonstrates core OOP concepts:

Encapsulation: Employee data is stored in private attributes with getter/setter methods.
Inheritance: Employee classes inherit from a common base class.
Abstraction: Abstract base class EmployeeBase defines required methods.
Polymorphism: Method show_info() is implemented differently across employee types if extended.


Features:

Add Employee: Enter details to save new employee.
Update Employee: Modify existing employee info.
Delete Employee: Remove employee by ID.
Search Employee: Find employee by ID instantly.
Show Full Info: View complete employee details in a pop-up.
Refresh Table: Reload all employee data
Data Persistence: Employee info stored in employees.csv.


Employee_Management_System_OOP
│
├── main.py                  # Run the application
├── employee_base.py         # Abstract base class
├── employee.py              # Employee base class
├── file_handler.py          # CSV operations
├── gui.py                   # GUI logic (Add, Update, Delete, Search, Full Info)
├── employees.csv            # Stored employee data
└── readme.md           # Project documentation



Concepts Used:

OOP: Classes, Encapsulation, Abstract Base Class (EmployeeBase)
File Handling: Read/Write CSV (EmployeeFileHandler)
GUI: Tkinter (EmployeeGUI) with tables, buttons, and pop-ups
Modular Structure: Separate files for clarity and maintenance


How to Run

Make sure you have Python 3.x installed.
Install Tkinter (usually comes with Python).
Open terminal or command prompt.
Navigate to project folder.
Run:
