class User:
    def __init__(self, name: str, age: int, sex: str, role: str):
        self.name = name
        self.age = int(age)
        self.sex = sex
        self.premium = False
        self.role = role

    def is_premium(self):
        return self.premium
