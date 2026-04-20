class EmployeeIn:
    def __init__(self):
        self.emp_id = 0
        self.name = ""
        self.basic = 0.0

    def inputDetails(self):
        self.emp_id = int(input("Enter Employee ID: "))
        self.name = input("Enter Name: ")
        self.basic = float(input("Enter Basic Salary: "))


class SalaryOut(EmployeeIn):
    def calculateSalary(self):
        self.hra = 0.20 * self.basic
        self.da = 0.10 * self.basic
        self.tax = 0.05 * self.basic

        self.gross = self.basic + self.hra + self.da
        self.net = self.gross - self.tax

    def displaySalary(self):
        print("\n--- Salary Details ---")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic)
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("Tax:", self.tax)
        print("Gross Salary:", self.gross)
        print("Net Salary:", self.net)


if __name__ == "__main__":
    emp = SalaryOut()
    emp.inputDetails()
    emp.calculateSalary()
    emp.displaySalary()