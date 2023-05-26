from entidades import Region
from datos.Dt_Region import Dt_Region


class Ng_Region:
    _dRegion = Dt_Region()

    def __init__(self):
        pass
    #-1: Error
    #1: Exito
    #2: Region ya existe
    def insertarRegion(self, Region_param):
        resultado = -1
        try:
            if self._dRegion.existeRegion(Region_param):
                resultado = 2
                return resultado

            if self._dRegion.insertarRegion(Region_param):
                resultado = 1
                return resultado

            return resultado

        except Exception as e:
            print("Negocio: Error en insertarRegion()", e)

    def actualizarRegion(self, Region_param):
        resultado = False
        try:
            resultado = self._dRegion.actualizarRegion(Region_param)
            return resultado

        except Exception as e:
            print("Negocio: Error en actualizarRegion()", e)


    def eliminarRegion(self, Region_param):
        resultado = False
        try:
            resultado = self._dRegion.eliminarRegion(Region_param)
            return resultado

        except Exception as e:
            print("Negocio: Error en eliminarRegion()", e)
