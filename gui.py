
import tkinter as tk
from tkinter import ttk, messagebox
from employee import Employee
from file_handler import EmployeeFileHandler

# ------------------------------
# GUI Application
# ------------------------------
class EmployeeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Saylani Mass IT Training - Employee Management System")
        self.root.geometry("800x550")  # adjusted width for Full Info button
        self.root.config(bg="#f5f5f5")

        self.employees = EmployeeFileHandler.load_all()

        # Default data if file empty
        if not self.employees:
            self.employees = [
                Employee("101", "Ayan hyder", "AI", "85000"),
                Employee("102", "saima baloch", "Data Science", "78000"),
                Employee("103", "M. Muzammil", "constructer", "90000")
            ]
            EmployeeFileHandler.save_all(self.employees)

        self.create_widgets()
        self.display_employees()

    def create_widgets(self):
        # Header
        tk.Label(
            self.root,
            text="Saylani Mass IT Training Department",
            font=("Arial", 18, "bold"),
            bg="#00b457",
            fg="white",
            pady=8
        ).pack(fill="x")

        tk.Label(
            self.root,
            text="Employee Management System",
            font=("Arial", 16, "bold"),
            bg="#2A7BCC",
            fg="white",
            pady=8
        ).pack(fill="x")

        # Input Frame
        form_frame = tk.Frame(self.root, bg="#ecf0f1", pady=10)
        form_frame.pack(fill="x")

        tk.Label(form_frame, text="ID:", font=("Arial", 12), bg="#ecf0f1").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#ecf0f1").grid(row=0, column=2, padx=10, pady=5)
        tk.Label(form_frame, text="Department:", font=("Arial", 12), bg="#ecf0f1").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(form_frame, text="Salary:", font=("Arial", 12), bg="#ecf0f1").grid(row=1, column=2, padx=10, pady=5)

        self.id_entry = tk.Entry(form_frame, width=15)
        self.name_entry = tk.Entry(form_frame, width=15)
        self.dept_entry = tk.Entry(form_frame, width=15)
        self.salary_entry = tk.Entry(form_frame, width=15)

        self.id_entry.grid(row=0, column=1)
        self.name_entry.grid(row=0, column=3)
        self.dept_entry.grid(row=1, column=1)
        self.salary_entry.grid(row=1, column=3)

        # Search Frame
        search_frame = tk.Frame(self.root, bg="#f5f5f5", pady=5)
        search_frame.pack(fill="x")

        tk.Label(search_frame, text="Search by ID:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=10)
        self.search_entry = tk.Entry(search_frame, width=20)
        self.search_entry.grid(row=0, column=1, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_emp, width=15, bg="#f39c12", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Clear Search", command=self.display_employees, width=15, bg="#7f8c8d", fg="white").grid(row=0, column=3, padx=5)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#f5f5f5")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Employee", command=self.add_emp, width=15, bg="#27ae60", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Employee", command=self.update_emp, width=15, bg="#2980b9", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Employee", command=self.delete_emp, width=15, bg="#c0392b", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.display_employees, width=15, bg="#8e44ad", fg="white").grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Full Info", command=self.show_full_info, width=15, bg="#f39c12", fg="white").grid(row=0, column=4, padx=5)

        # Table
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Dept", "Salary"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Dept", text="Department")
        self.tree.heading("Salary", text="Salary")
        self.tree.pack(fill="both", expand=True, pady=10)
        self.tree.bind("<ButtonRelease-1>", self.select_row)

    # ------------------------
    # Search Employee by ID
    # ------------------------
    def search_emp(self):
        search_id = self.search_entry.get().strip()
        if not search_id:
            messagebox.showwarning("Warning", "Enter Employee ID to search!")
            return

        filtered = [e for e in self.employees if e.get_id() == search_id]

        if not filtered:
            messagebox.showinfo("Not Found", f"No employee found with ID {search_id}")
            return

        # Display only searched employee
        for row in self.tree.get_children():
            self.tree.delete(row)
        for e in filtered:
            self.tree.insert("", "end", values=(e.get_id(), e.get_name(), e.get_dept(), e.get_salary()))

    # ------------------------
    # Show Full Info of Selected Employee
    # ------------------------
    def show_full_info(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select an employee from the table!")
            return

        values = self.tree.item(selected, 'values')
        emp_id = values[0]

        for e in self.employees:
            if e.get_id() == emp_id:
                info = (
                    f"Employee ID: {e.get_id()}\n"
                    f"Name: {e.get_name()}\n"
                    f"Department: {e.get_dept()}\n"
                    f"Salary: {e.get_salary()}"
                )
                messagebox.showinfo("Employee Full Info", info)
                return

    # ------------------------
    # Existing Methods
    # ------------------------
    def display_employees(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for e in self.employees:
            self.tree.insert("", "end", values=(e.get_id(), e.get_name(), e.get_dept(), e.get_salary()))

    def select_row(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.dept_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)
            self.id_entry.insert(0, values[0])
            self.name_entry.insert(0, values[1])
            self.dept_entry.insert(0, values[2])
            self.salary_entry.insert(0, values[3])

    def add_emp(self):
        emp_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        dept = self.dept_entry.get().strip()
        salary = self.salary_entry.get().strip()

        if not emp_id or not name or not dept or not salary:
            messagebox.showwarning("Warning", "All fields are required!")
            return

        for e in self.employees:
            if e.get_id() == emp_id:
                messagebox.showerror("Error", "Employee ID already exists!")
                return

        new_emp = Employee(emp_id, name, dept, salary)
        self.employees.append(new_emp)
        EmployeeFileHandler.save_all(self.employees)
        self.display_employees()
        messagebox.showinfo("Success", "Employee added successfully!")

    def update_emp(self):
        emp_id = self.id_entry.get().strip()
        for e in self.employees:
            if e.get_id() == emp_id:
                e.set_name(self.name_entry.get())
                e.set_dept(self.dept_entry.get())
                e.set_salary(self.salary_entry.get())
                EmployeeFileHandler.save_all(self.employees)
                self.display_employees()
                messagebox.showinfo("Success", "Employee updated successfully!")
                return
        messagebox.showerror("Error", "Employee not found!")

    def delete_emp(self):
        emp_id = self.id_entry.get().strip()
        for e in self.employees:
            if e.get_id() == emp_id:
                self.employees.remove(e)
                EmployeeFileHandler.save_all(self.employees)
                self.display_employees()
                messagebox.showinfo("Deleted", "Employee deleted successfully!")
                return
        messagebox.showerror("Error", "Employee not found!")


# ------------------------------
# Run the Application
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)







