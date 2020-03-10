class Miembro(object):
    
    def __init__(self, nombre, superior, subordinados, antiguedad):
        self.__subordinados = subordinados
        self.__nombre = nombre
        self.__antiguedad = antiguedad
        self.__superior = superior

    def getSubordinados(self):
        return self.__subordinados

    def setSubordinados(self, value):
        self.__subordinados = value
        
    def getSuperior(self):
        return self.__superior

    def setSuperior(self, value):
        self.__superior = value

    def getNombre(self):
        return self.__nombre

    def setNombre(self, value):
        self.__nombre = value

    def getAntiguedad(self):
        return self.__antiguedad

    def setAntiguedad(self, value):
        self.__antiguedad = value
    