class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
            return
        if self.peso >=8:
            print("GUAU, GUAU!")
        else:
            print("guau, guau")

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
   
   
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
        
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)    
    
    def pasear(self):
        print("Ayudo a mi dueño, {} a pasear".format(self.amo))
    
    def ladrar(self):
        if self.__trabajando:
            print("no puedo ladrar, estoy trabajando")
        else:
            Perro.ladrar(self)
            
            
    def trabajando(self, valor=None):
        
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
        
        
    
trek = Perro('Trek', 2, 30)

mia = Perro('Mia', 6, 1)

rantanplan = PerroAsistencia("Rantanplan", 4, 12, "Lucky Luke")


print(trek.nombre)
print(trek)
print(mia.edad)
print(mia.peso)
print(rantanplan)

trek.ladrar()
mia.ladrar()

rantanplan.pasear()
rantanplan.ladrar()
print(rantanplan.trabajando)
