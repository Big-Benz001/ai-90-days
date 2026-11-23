from dataclasses import dataclass
@dataclass
class Laptop:
    brand: str
    model: str
    price: float

laptop1 = Laptop("Hp","Notebook",600000)
laptop2 = Laptop("LG","openbook",400000)
laptop3 = Laptop("Dell","XPS",800000)

print(laptop1)
print(laptop2)
print(laptop3)