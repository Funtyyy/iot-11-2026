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
    """A fruit with a name, size, color and taste."""
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
    """A set of fruits with an optional topping."""
    def __init__(self, name: str = "Фруктовий салат"):
        self.name = name
        self.fruits = []
        self.topping = None

    def add(self, fruit: Fruit):
        self.fruits.append(fruit)

    def choose_topping(self) -> Topping:
        """Pick a topping that balances the salad's taste.

        Mostly sour salad -> sweet topping, mostly sweet salad -> sour
        topping, otherwise a neutral one. If several toppings match the
        needed taste, one is chosen at random.

        Raises:
            ValueError: if the salad has no fruits.
        """
        if not self.fruits:
            raise ValueError("Салат порожній, топінг обрати неможливо")

        sweet = sum(1 for f in self.fruits if f.taste == Taste.SWEET)
        sour = sum(1 for f in self.fruits if f.taste == Taste.SOUR)

        if sour > sweet:
            needed = Taste.SWEET
        elif sweet > sour:
            needed = Taste.SOUR
        else:
            needed = Taste.NEUTRAL

        candidates = [t for t in Topping if t.taste == needed]
        self.topping = random.choice(candidates)
        return self.topping

    def mix(self):
        """Shuffle the fruits in place."""
        random.shuffle(self.fruits)

    def __str__(self):
        lines = [f"{self.name}:"]
        lines += [f"\t{fruit}" for fruit in self.fruits]
        lines.append(f"\tТопінг: {self.topping if self.topping else 'немає'}")
        return "\n".join(lines)


def main():
    salad = FruitSalad("Літній мікс")

    salad.add(Fruit("яблуко", "medium", "зелений", Taste.SOUR))
    salad.add(Fruit("ківі", "small", "зелений", Taste.SOUR))
    salad.add(Fruit("банан", "medium", "жовтий", Taste.SWEET))
    salad.add(Fruit("груша", "medium", "жовтий", Taste.NEUTRAL))
    salad.add(Fruit("полуниця", "small", "червоний", Taste.SWEET))

    print(salad)

    print("\nПеремішуємо...\n")
    salad.mix()

    salad.choose_topping()
    print(salad)


if __name__ == "__main__":
    main()
