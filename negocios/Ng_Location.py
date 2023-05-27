from datos.Dt_Location import Dt_Location


class Ng_Location:
    dLocation = Dt_Location()

    def __init__(self):
        pass

    def agregarLocation(self, location_param):
        resultado = False
        try:
            if self.dLocation.agregarLocation(location_param):
                resultado = True

            return resultado
        except Exception as e:
           print("Negocio: Error insertarLocalización()", e)


    def actualizarLocalizacion(self, location_param):
        resultado = False
        try:
            if self.dLocation.actualizarLocation(location_param):
                resultado = True

            return resultado
        except Exception as e:
           print("Negocio: Error actualizarLocalización()", e)

    def eliminarLocalizacion(self, location_param):
        resultado = False
        try:
            if self.dLocation.eliminarLocation(location_param):
                resultado = True

            return resultado
        except Exception as e:
           print("Negocio: Error eliminarLocalización()", e)
