class FullName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee:
    def __init__(self, first_name, last_name, salary, address):
        self.full_name = FullName(first_name, last_name)
        self.salary = salary
        self.address = address

    def __str__(self):
        return (
            f"Employee Name   : {self.full_name}\n"
            f"Employee Address: {self.address}\n"
            f"Employee Salary : ${self.salary:,}"
        )

    def print_employee(self):
        print(self)

    def update_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
        else:
            print("Invalid salary!")

    def update_address(self, new_address):
        self.address = new_address


def read_employee():
    first_name = input("Enter employee's first name: ").strip()
    last_name = input("Enter employee's last name: ").strip()
    address = input("Enter employee's address: ").strip()

    while True:
        try:
            salary = int(input("Enter employee's salary: "))
            if salary <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number for salary.")

    return first_name, last_name, salary, address


first_name, last_name, salary, address = read_employee()
emp1 = Employee(first_name, last_name, salary, address)

emp1.print_employee()


