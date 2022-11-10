class ArbolBinario:

    def __init__(self, padre, dato):
        self.padre = padre
        self.dato = dato
        self.hijoIzq = None
        self.hijoDer = None

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def get_dato(self):
        return self.dato

    def set_dato(self, dato):
        self.dato = dato

    def get_hijoIzq(self):
        return self.hijoIzq

    def set_hijoIzq(self, hijoIzq):
        self.hijoIzq = hijoIzq

    def get_hijoDer(self):
        return self.hijoDer

    def set_hijoDer(self, hijoDer):
        self.hijoDer = hijoDer

    def mostrar(self):
        print(self.dato)
        if(self.hijoIzq != None):
            self.hijoIzq.mostrar()
        if(self.hijoDer != None):
            self.hijoDer.mostrar()

class ArbolN:

    def __init__(self, padre, dato):
        self.padre = padre
        self.dato = dato
        self.hijos = []

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def get_dato(self):
        return self.dato

    def set_dato(self, dato):
        self.dato = dato

    def get_hijos(self):
        return self.hijos

    def set_hijos(self, hijos):
        self.hijos = hijos

    def add_child(self,hijo):
        self.hijos.append(hijo)

    def mostrar(self):
        if (self.padre != None):
            print(f"{self.dato} y mi padre es {self.padre.dato}")
        else:
            print(f"{self.dato}")
        for n in self.hijos:
            n.mostrar()