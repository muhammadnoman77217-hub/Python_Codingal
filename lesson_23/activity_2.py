class vehicle :
    #constructer function
    def __init__(self,model,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.model = model

    def dist(self):
        return self.max_speed * self.mileage

BMW = vehicle("X9",240,80)

Audi = vehicle("R8",320,50)

print("BMW")
print("Model name : ",BMW.model)
print("Model top speed : ",BMW.max_speed)
print("Model mileage",BMW.mileage)
print("Maximum distance covered : ", BMW.dist())
print("\n\n")

print("Audi")
print("Model name : ",Audi.model)
print("Model top speed : ",Audi.max_speed)
print("Model mileage",Audi.mileage)
print("Maximum distance covered : ", Audi.dist())
print("\n\n")