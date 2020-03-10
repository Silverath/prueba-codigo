class Carcel(object):
    
    def __init__(self):
        self.__miembroEncarcelado = None

    def entrar(self, miembro):
        self.__miembroEncarcelado = miembro

    def salir(self):
        self.__miembroEncarcelado = None

    def getMiembroEncarcelado(self):
        return self.__miembroEncarcelado