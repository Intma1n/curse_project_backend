from database import GetUser, GetBudget, GetEquipment, GetReconstruction, RegistrationForReconstruction


class Singleton:
    def __init__(self):
        self.my_user = GetUser()
        self.my_budget = GetBudget()
        self.my_equipment = GetEquipment()
        self.my_reconstruction = GetReconstruction()
        self.my_register_for_rec = RegistrationForReconstruction()


singlton = Singleton()
