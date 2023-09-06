class Dog:
    def __init__(self, name="", breed=None):
        self._breed = None
        if name == "":
            print("Name must be string between 1 and 25 characters.")
        elif type(name) in (int, float):
            print("Name must be string between 1 and 25 characters.")
        elif len(name) > 25 :
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name
    def breed(self):
        return self._breed

    def set_breed(self, breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
        if breed in approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in the list of approved breeds.")




        
            
