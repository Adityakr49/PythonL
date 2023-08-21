class Car:
    wheels=4               #class variable
    def __init__(self,make,model,year,color): #like constructor
        self.make = make   #instance variable
        self.model = model #instance variable
        self.year = year   #instance variable
        self.color = color #instance variable

    # def drive(self): #self is like this of java
    #     print("The "+self.model +" is driving")
    #
    # def stop(self):
    #     print("The "+self.model +" is stopped")