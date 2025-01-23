class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be in list of pets.")
        if pet not in self.pets_list:
            self.pets_list.append(pet)

        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
        

class Pet:

    PET_TYPES = ["dog","cat","rodent","bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner 
        
        self.pet_type = pet_type if pet_type in Pet.PET_TYPES else None
        if self.pet_type is None:
            raise Exception("Pet must be on the list.")

        Pet.all.append(self)
        
       

       
