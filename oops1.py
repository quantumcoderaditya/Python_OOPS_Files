class Dog:

    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        

    def bark(self):
        print("Whoof Whoof!!!")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        
owner1 = Owner("Danny","122 Springfield Drive","888-999")

dog1=Dog("Bruce","Scottish Terrier",owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

owner2 = Owner("Sally","122 Springfield Drive","888-999")
dog2=Dog("Freya","Greyhound",owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.name)
print(dog2.owner.address)
print(dog2.owner.contact_number)
