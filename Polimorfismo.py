# --- Clase base ---
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Cada animal debe implementar su propio sonido.")

    def describir(self):
        return f"Soy {self.nombre} y hago: {self.hacer_sonido()}"


# --- Clases derivadas ---
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"


class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuu!"


class Pato(Animal):
    def hacer_sonido(self):
        return "¡Cuac!"


# Lista de distintos animales (polimorfismo en acción)
animales = [
    Perro("Rex"),
    Gato("Luna"),
    Vaca("Lola"),
    Pato("Donald"),
]

print("=" * 40)
print("  POLIMORFISMO: Sonidos de animales")
print("=" * 40)


for animal in animales:
    print(animal.describir())

print("=" * 40)


print("\nLlamada directa a hacer_sonido():")
for animal in animales:
    print(f"  {animal.nombre}: {animal.hacer_sonido()}")