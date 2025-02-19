class Profile:

    def __init__(self, surname):
        self.surname = surname

p = Profile("Mandela")
setattr(p, 'first_name', 'Rolihlahla')

print(p.first_name)
print(getattr(p, 'first_name'))
