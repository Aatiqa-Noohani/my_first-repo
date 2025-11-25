
import csv
from employee import Employee

# ------------------------------
# File Handler
# ------------------------------
class EmployeeFileHandler:
    file_name = "employees.csv"

    @staticmethod
    def save_all(employees):
        with open(EmployeeFileHandler.file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            for e in employees:
                writer.writerow([e.get_id(), e.get_name(), e.get_dept(), e.get_salary()])

    @staticmethod
    def load_all():
        emp_list = []
        try:
            with open(EmployeeFileHandler.file_name, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        emp_list.append(Employee(row[0], row[1], row[2], row[3]))
        except FileNotFoundError:
            pass
        return emp_list

