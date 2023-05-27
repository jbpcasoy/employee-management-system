from employee import Employee
class EMS:
    def __init__(self):
        self.employees: list[Employee] = []
    
    def add_employee(self, employee:Employee):
        self.employees.append(employee)
        
    def view_employee(self, id:int):
        return self.employees[id]
        
    def view_employees(self, page:int=1, page_size:int=10):
        if len(self.employees) < 1:
            return {}
        
        if page_size < len(self.employees):
            start = page_size * (page - 1)
            end = page_size * page
        else:
            start = len(self.employees) * (page - 1)
            end = len(self.employees) * page
        
        return {i: self.employees[i] for i in range(start, end)}

    def edit_employee(self, id:int, employee:Employee):
        self.employees[id] = employee
    
    def delete_employee(self, id: int): 
        self.employees.pop(id)