

class Employee():
    def __init__(self,id,name,address):
        self.name = name
        self.id = id
        self.address = address
        
    def display(self):
        print("Your Name is ",self.name)
        print("Your id is ",self.id)
        print("Your address is ",self.address)
        
emp = Employee(10, "Sagar Neupane", "Kohalpur-12,Banke,Nepal")