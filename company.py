from employee import Employee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_pay_details(self, amount):
        for employee in self.employees:
            employee.display_pay_details(amount)


def main():
    company = Company()

    emp1 = Employee("Alice", "Software Engineer", 90000)
    emp2 = Employee("Bob", "Data Scientist", 95000)
    emp3 = Employee("Charlie", "Product Manager", 105000)
    emp4 = Employee("Diana", "UX Designer", 85000)
    emp5 = Employee("Ethan", "DevOps Engineer", 92000)

    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)
    company.add_employee(emp4)
    company.add_employee(emp5)

    company.display_all_pay_details(5000)


if __name__ == "__main__":
    main()