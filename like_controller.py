from database import GetUser, GetBudget, GetEquipment


class Singleton:
    def __init__(self):
        self.my_user = GetUser()
        self.my_budget = GetBudget()
        self.my_equipment = GetEquipment()


singlton = Singleton()
