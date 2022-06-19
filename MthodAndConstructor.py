class DemoClass:
    a = 10
    #  Defining Constructor
    def __init__(self):
         print("Welcome to Bhopal")

    def showvalue(self):
        # Self.variable name is Mandatory for creating variable or printing ans
        self.c = self.a * self.a
        print(self.c)

    def showvalue1(self):
        print("Welcome")

    def showvalue2(self,a,b):
        print(a+b)


# Creating obj as object of class DemoClass
obj = DemoClass()
# calling function
obj.showvalue()
obj.showvalue1()

# passing arguments in showvalue2 . 20 will be store in a and 30 will store in b.
obj.showvalue2(20,30)