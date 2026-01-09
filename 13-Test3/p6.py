class C():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        initials = self.name[0] + self.surname[0] + str(self.age)
        if self.age<18:
            initials = initials.lower()
        return initials
print(C("John","May",21))


