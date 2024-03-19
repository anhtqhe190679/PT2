class Employee:
    def __init__(self, code, name, salary, allowance):
        self.code = code
        self.name = name
        self.salary = salary
        self.allowance = allowance

def add_employee(employee, filename):
    with open(filename, 'a') as file:
        file.write(f"{employee.code},{employee.name},{employee.salary},{employee.allowance}\n")

def binary_search_by_name(employees, name):
    left, right = 0, len(employees) - 1
    while left <= right:
        mid = (left + right) // 2
        if employees[mid].name == name:
            return employees[mid]
        elif employees[mid].name < name:
            left = mid + 1
        else:
            right = mid - 1
    return None

def remove_employee(code, filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if not line.startswith(f"{code},"):
                file.write(line)

def print_sorted_by_salary_allowance(employees, filename):
    sorted_employees = sorted(employees, key=lambda x: x.salary + x.allowance, reverse=True)
    with open(filename, 'w') as file:
        for employee in sorted_employees:
            file.write(f"{employee.code},{employee.name},{employee.salary},{employee.allowance}\n")

def read_employees(filename):
    employees = []
    with open(filename, 'r') as file:
        for line in file:
            code, name, salary, allowance = line.strip().split(',')
            employees.append(Employee(code, name, float(salary), float(allowance)))
    return employees

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add New Employee")
        print("2. Find Employee by Name")
        print("3. Remove Employee by Code")
        print("4. Print Sorted List by Salary + Allowance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            code = input("Enter employee code: ")
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            allowance = float(input("Enter employee allowance: "))
            new_employee = Employee(code, name, salary, allowance)
            add_employee(new_employee, "input.txt")
            print("Employee added successfully.")

        elif choice == "2":
            name = input("Enter employee name to search: ")
            employees_list = read_employees("input.txt")
            searched_employee = binary_search_by_name(employees_list, name)
            if searched_employee:
                print("Employee found:")
                print(f"Code: {searched_employee.code}")
                print(f"Name: {searched_employee.name}")
                print(f"Salary: {searched_employee.salary}")
                print(f"Allowance: {searched_employee.allowance}")
            else:
                print("Employee not found.")

        elif choice == "3":
            code = input("Enter employee code to remove: ")
            remove_employee(code, "input.txt")
            print("Employee removed successfully.")

        elif choice == "4":
            employees_list = read_employees("input.txt")
            print_sorted_by_salary_allowance(employees_list, "result.txt")
            print("Sorted list printed and saved successfully.")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
