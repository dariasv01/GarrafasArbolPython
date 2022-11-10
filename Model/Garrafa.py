class Garrafa:
    def __init__(self, capacidad, capacidadMax):
        self.capacidad = capacidad
        self.capacidadMax = capacidadMax

    def get_capacidadMax(self):
        return self.capacidadMax

    def get_capacidad(self):
        return self.capacidad

    def set_capacidadMax(self, capacidadMax):
        self.capacidadMax = capacidadMax

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad

    def vaciar(self):
        self.capacidad = 0

    def llenar(self):
        self.capacidad = self.capacidadMax