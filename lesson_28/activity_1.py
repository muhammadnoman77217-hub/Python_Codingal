# Class creation
class myClass:

    # private variable
    def __priMeth(self):
        print("I'm inside class myClass")

    # Function to print value of private variable
    def hello(self):
        print("Private Variable Value: " ,myClass.__privateVar)

# Object creation and method call
foo = myClass()
foo.hello()
foo.__priMeth