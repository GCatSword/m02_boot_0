class Perro():
    def __init__(self, nombre, edad, peso):        
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >=8:
            print("GUAU, GUAU!")
        else:
            print("guau, guau")

    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)
        
        

trek = Perro('Trek', 2, 30)

mia = Perro('Mia', 6, 1)

print(trek.nombre)
print(trek)
print(mia.edad)
print(mia.peso)

trek.ladrar()
mia.ladrar()
