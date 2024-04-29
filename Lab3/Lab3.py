import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER, department TEXT, salary REAL)''')

class Employee:
    all_employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.all_employees.append(self)
        
        c.execute("INSERT INTO employees (first_name, last_name, age, department, salary) VALUES (?, ?, ?, ?, ?)",
                  (self.first_name, self.last_name, self.age, self.department, self.salary))
        conn.commit()

    def transfer(self, new_department):
        self.department = new_department
        c.execute("UPDATE employees SET department = ? WHERE first_name = ? AND last_name = ?",
                  (self.department, self.first_name, self.last_name))
        conn.commit()

    def fire(self):
        Employee.all_employees.remove(self)
        c.execute("DELETE FROM employees WHERE first_name = ? AND last_name = ?", (self.first_name, self.last_name))
        conn.commit()

    def show(self):
        print("Name:", self.first_name, self.last_name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Salary:", self.salary)

    @classmethod
    def list_employees(cls):
        for emp in cls.all_employees:
            emp.show()

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print("Name:", self.first_name, self.last_name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Managed Department:", self.managed_department)
        print("Salary: Confidential")

def main():
    while True:
        print("\nMenu:")
        print("1. Add new employee (e) or manager (m)")
        print("2. Transfer employee.")
        print("3. Fire employee.")
        print("4. Show employee details (e/m)")
        print("5. List all employees (e/m)")
        print("6. Quit (q)")

        choice = input("Enter your choice: ")

        if choice.lower() == 'q':
            break
        elif choice.lower() == 'e' or choice.lower() == 'm':
            if choice.lower() == 'm':
                first_name = input("Enter manager's first name: ")
                last_name = input("Enter manager's last name: ")
                age = int(input("Enter manager's age: "))
                department = input("Enter manager's department: ")
                salary = float(input("Enter manager's salary: "))
                managed_department = input("Enter managed department: ")
                manager = Manager(first_name, last_name, age, department, salary, managed_department)
            else:
                first_name = input("Enter employee's first name: ")
                last_name = input("Enter employee's last name: ")
                age = int(input("Enter employee's age: "))
                department = input("Enter employee's department: ")
                salary = float(input("Enter employee's salary: "))
                employee = Employee(first_name, last_name, age, department, salary)

        elif choice.lower() == '2':
            name = input("Enter employee's first name: ")
            last_name = input("Enter employee's last name: ")
            new_department = input("Enter new department: ")
            for emp in Employee.all_employees:
                if emp.first_name == name and emp.last_name == last_name:
                    emp.transfer(new_department)
                    print("Employee transferred successfully.")
                    break
            else:
                print("Employee not found.")

        elif choice.lower() == '3':
            name = input("Enter employee's first name: ")
            last_name = input("Enter employee's last name: ")
            for emp in Employee.all_employees:
                if emp.first_name == name and emp.last_name == last_name:
                    emp.fire()
                    print("Employee fired successfully.")
                    break
            else:
                print("Employee not found.")

        elif choice.lower() == '4':
            name = input("Enter employee's first name: ")
            last_name = input("Enter employee's last name: ")
            for emp in Employee.all_employees:
                if emp.first_name == name and emp.last_name == last_name:
                    emp.show()
                    break
            else:
                print("Employee not found.")

        elif choice.lower() == '5':
            Employee.list_employees()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
