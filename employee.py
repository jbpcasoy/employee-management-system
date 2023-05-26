class Employee:
    def __init__(self, name, address, number, email, salary):
        self.name = name
        self.address = address
        self.number = number
        self.email = email
        self.salary = salary

    def __repr__(self) -> str:
        return "{{\nName: {},\nAddress: {},\nNumber: {},\nEmail: {},\nSalary: {},\n}}".format(self.name, self.address, self.number, self.email, self.salary)