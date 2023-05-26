class EMS:
    
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def view_employees(self, page=1, page_size=10):
        start = page_size * (page - 1)
        end = page_size * page
        return self.employees