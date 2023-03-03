
class Pizza:
    def __init__(self):
        self._description = "Pizza"
        self._cost = 0

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Klasik Pizza"
        self._cost = 20


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Margherita Pizza"
        self._cost = 25


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Turk Pizza"
        self._cost = 30


class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._description = "Sade Pizza"
        self._cost = 15


class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component

    def get_description(self):
        return self.component.get_description() + " + " + self._description

    def get_cost(self):
        return self.component.get_cost() + self._cost


class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Zeytin"
        self._cost = 3


class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Mantarlar"
        self._cost = 3


class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Keci Peyniri"
        self._cost = 5


class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Et"
        self._cost = 7


class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Sogan"
        self._cost = 2


class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self._description = "Misir"
        self._cost = 2
