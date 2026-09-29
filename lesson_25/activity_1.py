from abc import ABC, abstractclassmethod
class vehicle(ABC) :
    def __init__(self,model):
        self.model=model

    @abstractclassmethod
    def enter_details(self):
        pass

class car(vehicle):
    def __init__(self, model):
        super().__init__(model)

    def enter_details(self):
        self.tyres=4
        self.color=input("enter color")

class bike(vehicle):
    def __init__(self, model):
        super().__init__(model)

    def enter_details(self):
        self.tyres=2
        self.color=input("enter color")

BMW=car("x9")
ducati=bike("f9")
