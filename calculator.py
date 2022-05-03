
class Calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"the value of {self.number} square is {self.number**2}")

    def squareRoot(self):
        print(f"the value of {self.number} squareRoot is {self.number**0.5}")

    def cube(self):
        print(f"the value of {self.number} cube is {self.number**3}")

calculate= Calculator(9)
calculate.square()
calculate.squareRoot()
calculate.cube()

        
     