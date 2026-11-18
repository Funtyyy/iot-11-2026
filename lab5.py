import random
from enum import Enum


class Taste(Enum):
    SWEET = "солодкий"
    SOUR = "кислий"
    NEUTRAL = "нейтральний"


class Topping(Enum):
    HONEY = ("мед", Taste.SWEET)
    CARAMEL = ("карамель", Taste.SWEET)
    LEMON_JUICE = ("лимонний сік", Taste.SOUR)
    YOGURT = ("йогурт", Taste.NEUTRAL)
    NUTS = ("горіхи", Taste.NEUTRAL)

    def __init__(self, title: str, taste: Taste):
        self.title = title
        self.taste = taste

    def __str__(self):
        return f"{self.title} ({self.taste.value})"


class Fruit:

    def __init__(self,
                 name: str = "",
                 size: str = "medium",
                 color: str = "",
                 taste: Taste = Taste.NEUTRAL):
        self.name = name
        self.size = size
        self.color = color
        self.taste = taste

    def __str__(self):
        return f"{self.name} ({self.color}, {self.size}, {self.taste.value})"


class FruitSalad:

    def __init__(self,
                 name: str = "Фруктовий салат"):
        self.name = name
        self.fruits = []
        self.topping = None

    def add(self, fruit: Fruit):
        self.fruits.append(fruit)

    def choose_topping(self):
        if not self.fruits:
            raise ValueError("Салат порожній, топінг обрати неможливо")

        sweet = sum(1 for f in self.fruits if f.taste == Taste.SWEET)
        sour = sum(1 for f in self.fruits if f.taste == Taste.SOUR)

        if sour > sweet:
            self.topping = Topping.HONEY
        elif sweet > sour:
            self.topping = Topping.LEMON_JUICE
        else:
            self.topping = Topping.YOGURT

        return self.topping

    def mix(self):
        random.shuffle(self.fruits)

    def print_salad(self):
        print(f"{self.name}:")
        for fruit in self.fruits:
            print(f"\t{fruit}")
        print(f"\tТопінг: {self.topping if self.topping else 'немає'}")


def main():
    salad = FruitSalad("Літній мікс")

    salad.add(Fruit("яблуко", "medium", "зелений", Taste.SOUR))
    salad.add(Fruit("ківі", "small", "зелений", Taste.SOUR))
    salad.add(Fruit("банан", "medium", "жовтий", Taste.SWEET))
    salad.add(Fruit("груша", "medium", "жовтий", Taste.NEUTRAL))
    salad.add(Fruit("полуниця", "small", "червоний", Taste.SWEET))

    salad.print_salad()

    print("\nПеремішуємо...\n")
    salad.mix()

    salad.choose_topping()
    salad.print_salad()


if __name__ == "__main__":
    main()