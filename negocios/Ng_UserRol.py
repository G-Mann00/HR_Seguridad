from datos.Dt_tbl_UserRol import Dt_tbl_UserRol
from entidades.Tbl_UserRol import Tbl_UserRol

class Ng_UserRol:
    dUserRol = Dt_tbl_UserRol() #Datos
    UR = Tbl_UserRol() #Entidades

    def __init__(self):
        pass

    # -1 = Error
    # 1 = Exito
    def actualizarUserRol(self, UserRol_param):
        resultado = -1
        try:
            if self.dUserRol.actualizarUserRol(UserRol_param):
                resultado = 1

            return resultado

        except Exception as e:
            print("Negocio: Error en actualizarUserRol()", e)
