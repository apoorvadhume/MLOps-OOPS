# Initiate a class
class employee:
    #spl. method/ magic method/ dunder method - constructor
    def __init__(self):
        print("Started executing attributrs/ data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attribute/ data have been onitiated")

    # Prepare a function Travel
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# Creating an object or instance of a class
sam = employee()

# Printing Attributes
print(sam.salary)

# Calling the method
sam.travel("Kerala")

# What is the type of this class?
print(type(sam))