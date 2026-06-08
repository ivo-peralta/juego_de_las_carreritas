
class Personaje:
    estado = True

    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza

    def correr(self, distancia):
        if Personaje.estado:
            tiempo = distancia / self.velocidad
            print(f"{self.nombre} corrió {distancia} metros en {tiempo:.2f} segundos.")
            self.resistencia -= distancia * 0.1
            if self.resistencia <= 0:
                Personaje.estado = False
                print(f"{self.nombre} se ha agotado y no puede continuar.")
        else:
            print(f"{self.nombre} no puede correr porque está agotado.")

    def recuperarse(self):
        if not Personaje.estado:
            self.resistencia += 10
            if self.resistencia > 100:
                self.resistencia = 100
            print(f"{self.nombre} se ha recuperado. Resistencia actual: {self.resistencia}.")
            if self.resistencia > 0:
                Personaje.estado = True
        else:
            print(f"{self.nombre} no puede recuperarse porque está vivo.")

        