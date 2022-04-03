class Buss:
    def __init__(self, doors, color, motor):
        self.doors = doors
        self.color = color
        self.motor = motor

    def __repr__(self):
        return f'\n{self.__class__.__name__:-^10}' + f'\nDoors: {self.doors}\nColor: {self.color}\nMotor: {self.motor}\n' \
                                                     f'{"Extra":-^10}'


class Buss1(Buss):
    def __init__(self, doors, color, motor, name, _type):
        super().__init__(doors, color, motor)
        self.name = name
        self._type = _type

    def __repr__(self):
        return super().__repr__() + f'\nName: {self.name}\nType: {self._type}'


buss = Buss(4, 'black', 'type 1')
print(buss)
buss1 = Buss1(5, 'white', 'type 5', 'seila', 'Buss_2')
print(buss1)

