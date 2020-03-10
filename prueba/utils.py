from miembro import Miembro
from carcel import Carcel
import json

def creacionListadoMiembrosJSON():
    listadoMiembros = ()
    listadoFinal = []
    with open('datos.json', 'r') as f:
        listadoMiembros = json.load(f)
    for miembro in listadoMiembros['members']:
        nuevoMiembro = Miembro(miembro['name'], miembro['boss'], miembro['subordinates'], miembro['seniority'])
        listadoFinal.append(nuevoMiembro)
    
    return listadoFinal

def reubicarTrasEncarcelamiento(carcel, miembros):
    miembrosMismoNivel = []
    for miembroBanda in miembros:
        if miembroBanda.getSuperior() == carcel.getMiembroEncarcelado().getSuperior:
            miembrosMismoNivel.append(miembroBanda)
    if len(miembrosMismoNivel) >= 0:
        antiguedad = 0
        miembroSeleccionado = Miembro('', '', [], 0)
        for miembroMismoNivel in miembrosMismoNivel:
            if miembroMismoNivel.getAntiguedad() >= antiguedad:
                antiguedad = miembroMismoNivel.getAntiguedad()
                miembroSeleccionado = miembroMismoNivel
        subordinados = miembroSeleccionado.getSubordinados()
        subordinados.append(carcel.getMiembroEncarcelado().getSubordinados())
        miembroSeleccionado.setSubordinados(subordinados)
        for miembro in miembros:
            if miembro.getNombre() in miembroSeleccionado.getSubordinados():
                miembro.setSuperior(miembroSeleccionado.getNombre())
        miembros.remove(carcel.getMiembroEncarcelado())
    else:
        antiguedad = 0
        miembroSeleccionado = Miembro('', '', [], 0)
        for miembro in miembros:
            if miembro.getNombre() in miembroSeleccionado.getSubordinados():
                if miembro.getAntiguedad() > antiguedad:
                    miembroSeleccionado = miembro
        subordinadosATraspasar = carcel.getMiembroEncarcelado().getSubordinados()
        subordinadosATraspasar.remove(carcel.getMiembroEncarcelado().getNombre())
        subordinadosMiembroElegido = miembroSeleccionado.getSubordinados()
        subordinadosMiembroElegido.append(subordinadosATraspasar)
        miembroSeleccionado.setSubordinados(subordinadosMiembroElegido)
        miembroSeleccionado.setSuperior(carcel.getMiembroEncarcelado().getSuperior())
        miembros.remove(carcel.getMiembroEncarcelado())

def getMasAltoCargo(miembros):
    for miembro in miembros:
        if miembro.getSuperior() == "":
            return miembro

def mostrarMiembrosPorConsola(miembros):
    for miembro in miembros:
        print("----------------------------------------------------------------------------------------------")
        print(miembro.getNombre())
        print(miembro.getAntiguedad())
        print(miembro.getSuperior())
        print(miembro.getSubordinados())