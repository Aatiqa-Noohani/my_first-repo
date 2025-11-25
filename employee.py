from employee_base import EmployeeBase

# ------------------------------
# Employee Class (Encapsulation)
# ------------------------------
class Employee(EmployeeBase):
    def __init__(self, emp_id, name, dept, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__dept = dept
        self.__salary = salary

    # Getters
    def get_id(self): return self.__emp_id
    def get_name(self): return self.__name
    def get_dept(self): return self.__dept
    def get_salary(self): return self.__salary

    # Setters
    def set_name(self, name): self.__name = name
    def set_dept(self, dept): self.__dept = dept
    def set_salary(self, salary): self.__salary = salary

    def show_info(self):
        return f"{self.__emp_id} - {self.__name} - {self.__dept} - {self.__salary}"
