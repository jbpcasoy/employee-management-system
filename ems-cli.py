from ems import EMS 
from employee import Employee

ems = EMS()

def get_action():
    print("=============Employee Management System=============")
    print("Actions:")
    print("[1]: Add Employee")
    print("[2]: View Employee")
    print("[3]: Edit Employee")
    print("[4]: Delete Employee")
    print("Choose action (1/2/3/4):", end=" ")
    
    try:
        action = int(input())
    except ValueError:
        print("Invalid value!")
        return
    
    return action

def add_employee(ems):
    print("=============Input Employee Information=============")
    print("Name:", end=" ")
    name = input()
    print("Address:", end=" ")
    address = input()
    print("Number:", end=" ")
    number = input()
    print("Email:", end=" ")
    email = input()
    print("Salary:", end=" ")
    salary = float(input())
    
    employee = Employee(name, address, number, email, salary)
    print(employee)
    ems.add_employee(employee)
    
def view_employees(ems):
    print(ems.view_employees())
    
    
def main(ems):
    stop = False
    action = get_action()
    
    if action == 1:
        add_employee(ems)
    elif action == 2:
        view_employees(ems)
    else:
        print("Invalid action!")
    
    while not stop:
        main(ems)
    
main(ems)