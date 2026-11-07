class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_pay_details(self, amount):
        old_salary = self.salary
        self.salary += amount
        weekly_salary = self.salary / 52

        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Previous Salary: ${old_salary:.2f}")
        print(f"Pay Rise: ${amount:.2f}")
        print(f"New Annual Salary: ${self.salary:.2f}")
        print(f"Weekly Wage: ${weekly_salary:.2f}")
        print("------------------------------")