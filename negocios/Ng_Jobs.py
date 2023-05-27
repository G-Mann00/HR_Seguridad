from datos.Dt_Jobs import Dt_Jobs


class Ng_Jobs:
    _dJobs = Dt_Jobs()


    def __init__(self):
        pass

    # -1: Error
    # 1: Exito
    # 2: Ya existe
    def insertarTrabajo(self, Jobs_param):
        resultado = -1
        try:

            if self._dJobs.existeTrabajo(Jobs_param):
                resultado = 2
                return resultado

            if self._dJobs.insertarTrabajo(Jobs_param):
                resultado = 1
                return resultado

            return resultado

        except Exception as e:
            print("Negocio: Error en insertarTrabajo()", e)

    def actualizarTrabajo(self, Jobs_param):
        resultado = False
        try:
            resultado = self._dJobs.actualizarTrabajo(Jobs_param)
            return resultado

        except Exception as e:
            print("Negocio: Error en actualizarTrabajo()", e)

    def eliminarTrabajo(self, Jobs_param):
        resultado = False
        try:
            resultado = self._dJobs.eliminarTrabajo(Jobs_param)
            return resultado

        except Exception as e:
            print("Negocio: Error en eliminarTrabajo()", e)
