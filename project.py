
print("Welcome to Aylin's Rent A Car ")
is_rented=input("Please select the car you want to rent; Toyota,Bmw,Ford: ").capitalize()


class Car:
    car_status={"Toyota":False,"Bmw":False,"Ford":False}
    def __init__(self,brand,model,plate):
     self.brand=brand
     self.model=model
     self.plate=plate
     
     
    
    def rent_car(self):
        if Car.car_status[self.brand]==False:
            print("{},{},{} already rented by someone else".format(self.brand,self.model,self.plate))
        else:
        
            print("You have rented {},{},{} ".format(self.brand,self.model,self.plate))
            Car.car_status[self.brand] = True
            
first_car=Car("Toyota","Corolla","34ABC123")
second_car=Car("Bmw","320i","35XYZ987") 
third_car=Car("Ford","Focus","62DEF456")

selected_car = None
if is_rented == "Toyota":
    selected_car = first_car
elif is_rented == "Bmw":
        selected_car = second_car
elif is_rented == "Ford":
        selected_car = third_car
        
    
if selected_car:
    selected_car.rent_car()

