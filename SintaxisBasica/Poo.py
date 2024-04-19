#vamos a redactar la sintaxis para una clase
class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha= False 

    def arrancar(self):
        if self.enmarcha == False : 

            self.enmarcha= True
            print('el carro se puso en marcha')
        else:
            print('el carro ya esta encendido')
        pass 
    def getEstado(self):
        if self.enmarcha == True:
            print('el coche esta arrancado')
        else:
            print('el aun no se arranca')



miCoche = Coche()

miCoche.getEstado()
miCoche.arrancar()
miCoche.getEstado()
miCoche.arrancar()


