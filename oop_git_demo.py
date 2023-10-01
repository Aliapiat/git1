def git_sum(x, y):
    return x + y

class User:
    id = 0

    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gander = gender
        self._age = age

        User.id += 1
        self._id = User.id

    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            raise ValueError('Incorrect input')

    def get_id(self):
        return self._id

    def greet(self):
        print(f'Privet, {self.name}, {self.surname}!')

    def ismale(self):
        return self.gender == 'm'

    def isfemale(self):
        return self.gender == 'w'

    def __str__(self):
        return f'{self.name} {self.surname}'

class PremiumUser(User):

    def set_description(self, description):
        self.description = description

    def greet(self):
        print(f'Privet, {self.name}, {self.surname} GOLD!')

user = User('Ivan', 'Ivanovi4', 'm', 25)
pr_user = PremiumUser('Ulya', 'Ivanovna', 'w', 33)

print(PremiumUser.greet(pr_user))
