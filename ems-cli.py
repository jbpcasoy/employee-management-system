from ems import EMS
from employee import Employee
import getpass
import os
import dotenv

dotenv.load_dotenv()

ems = EMS()


def get_action():
    print("=============Employee Management System=============")
    print("Actions:")
    print("[1]: Add Employee")
    print("[2]: View Employee")
    print("[3]: Edit Employee")
    print("[4]: Delete Employee")
    print("[5]: Exit")

    try:
        action = int(input("Choose action: "))
    except ValueError:
        print("Invalid value!")
        return

    return action


def add_employee(ems: EMS):
    print("=============Add Employee=============")
    name = input("Name: ")
    address = input("Address: ")
    number = input("Number: ")
    email = input("Email: ")
    salary = float(input("Salary: "))

    employee = Employee(name, address, number, email, salary)
    print(employee)
    ems.add_employee(employee)


def view_employees(ems: EMS):
    print("=============View Employee=============")
    page = 1
    page_size = 10
    try:
        page = int(input("Page ({}): ".format(page)))
    except ValueError:
        pass

    try:
        page_size = int(input("Page Size ({}): ".format(page_size)))
    except ValueError:
        pass

    print(ems.view_employees(page=page, page_size=page_size))


def update_employee(ems: EMS):
    print("=============Update Employee=============")
    id = int(input("ID: "))
    try:
        old_employee = ems.view_employee(id)
    except IndexError:
        print("Invalid ID!")
        return

    name = input("Name ({}): ".format(old_employee.name))
    if name == "":
        name = old_employee.name

    address = input("Address ({}): ".format(old_employee.address))
    if address == "":
        address = old_employee.address

    number = input("Number ({}): ".format(old_employee.number))
    if number == "":
        number = old_employee.number

    email = input("Email ({}): ".format(old_employee.email))
    if email == "":
        email = old_employee.email

    salary = old_employee.salary
    try:
        salary = float(input("Salary ({}): ".format(old_employee.salary)))
    except ValueError:
        pass

    employee = Employee(name, address, number, email, salary)
    print(employee)
    ems.edit_employee(id, employee)


def delete_employee(ems: EMS):
    print("=============Delete Employee=============")
    id = int(input("ID: "))
    try:
        employee = ems.view_employee(id)
        print(employee)
    except IndexError:
        print("Invalid ID!")
        return

    confirm = "no"
    confirm = input("This action cannot be undone, are you sure? (yes|NO):")
    if confirm.lower() == "no" or confirm == "":
        print("Deletion cancelled!")
        return

    try:
        ems.delete_employee(id)
        print("Employee deleted successfully!")
    except IndexError:
        print("Invalid ID!")


def main(ems: EMS):
    stop = False

    # Authenticate
    user = input("Username: ")
    password = getpass.getpass("Password: ")

    if user != os.getenv("ADMIN_USER"):
        print("Username incorrect!")
        stop = True
    if password != os.getenv("ADMIN_PASSWORD"):
        print("Password incorrect!")
        stop = True
    if user == os.getenv("ADMIN_USER") and password == os.getenv("ADMIN_PASSWORD"):
        print("Access granted!")

    if stop:
        return

    action = get_action()

    if action == 1:
        add_employee(ems)
    elif action == 2:
        view_employees(ems)
    elif action == 3:
        update_employee(ems)
    elif action == 4:
        delete_employee(ems)
    elif action == 5:
        stop = True
    else:
        print("Invalid action!")

    if not stop:
        main(ems)


main(ems)
