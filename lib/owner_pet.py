class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception(f"Invalid pet type '{pet_type}'. Valid pet types are {Pet.PET_TYPES}.")

        if owner:
            owner.add_pet(self)

        Pet.all.append(self)
        

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only objects of type 'Pet' can be added.")
        pet.owner = self
        if pet not in self.pets_list:
            self.pets_list.append(pet)


    def pets(self):
        return self.pets_list

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
