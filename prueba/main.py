from carcel import Carcel
from miembro import Miembro
import utils

listadoDeMiembros = utils.creacionListadoMiembrosJSON()
carcel = Carcel()
for miembro in listadoDeMiembros:
    if miembro.getNombre() == 'Jhon':
        carcel.entrar(miembro)
utils.reubicarTrasEncarcelamiento(carcel, listadoDeMiembros)
print("----------MIEMBROS DESPUES DEL ENCARCELAMIENTO DE JHON----------")
utils.mostrarMiembrosPorConsola(listadoDeMiembros)
carcel.salir()
listadoDeMiembros = utils.creacionListadoMiembrosJSON()
print("----------MIEMBROS DESPUES DE DEJAR LIBRE AL ENCARCELADO JHON----------")
utils.mostrarMiembrosPorConsola(listadoDeMiembros)

jefe = utils.getMasAltoCargo(listadoDeMiembros)
carcel.entrar(jefe)
utils.reubicarTrasEncarcelamiento(carcel, listadoDeMiembros)
print("----------MIEMBROS DESPUES DEL ENCARCELAMIENTO DEL JEFE SUPREMO----------")
utils.mostrarMiembrosPorConsola(listadoDeMiembros)
carcel.salir()
listadoDeMiembros = utils.creacionListadoMiembrosJSON()
print("----------MIEMBROS DESPUES DE DEJAR LIBRE AL JEFE SUPREMO----------")
utils.mostrarMiembrosPorConsola(listadoDeMiembros)