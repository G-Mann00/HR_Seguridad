from datos.Dt_Country import Dt_Country
from entidades.Country import Country


class Ng_Country:
    dCountry = Dt_Country()
    c = Country()

    def __init__(self):
        pass

    # -1 = Error
    # 1 = Exito
    # 2 = Existe un registro con el mismo identificador
    # 3 = Existe un registro con el mismo nombre
    def insertarPais(self, pais_param):
        resultado = -1
        try:
            if self.dCountry.validarIdUnico(pais_param):
                resultado = 2
                return resultado

            if self.dCountry.existePais(pais_param):
                resultado = 3
                return resultado

            if self.dCountry.insertarPais(pais_param):
                resultado = 1
            return resultado
        except Exception as e:
            print("Negocio: Error en insertarPais()", e)


    def actualizarPais(self, pais_param):
        resultado = False
        try:
            if self.dCountry.actualizarPais(pais_param):
                resultado = True
            return resultado
        except Exception as e:
            print("Negocio: Error en actualizarPais()", e)

    def eliminarPais(self, pais_param):
        resultado = False
        try:
            if self.dCountry.eliminarPais(pais_param):
                resultado = True
            return resultado
        except Exception as e:
            print("Negocio: Error en eliminarPais()", e)

