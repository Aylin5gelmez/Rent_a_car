
print("Welcome to Aylin's Rent A Car ")
is_rented=input("Please Kiralamak istediğiniz aracı seçin ;Toyoto,Honda,BMW: ").capitalize
class Car:
    def __init__(self,brand,model,plate):
     self.brand=brand
     self.model=model
     self.plate=plate
     self.is_rented:False
    
    def rent_car(self):
        if self.is_rented:
            return "{},{},{} zaten kiralanmış".format(self.brand,self.model,self.plate)
        