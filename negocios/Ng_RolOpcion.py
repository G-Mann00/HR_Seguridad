from datos.Dt_tbl_RolOpcion import Dt_tbl_RolOpcion
from entidades.Tbl_rolOpcion import Tbl_rolOpcion

class Ng_RolOpcion:
    dRolOpcion = Dt_tbl_RolOpcion() #Datos
    RO = Tbl_rolOpcion() #Entidades

    def __init__(self):
        pass

    # -1 = Error
    # 1 = Exito
    # 2 = Existe un registro con el mismo identificador
    # 3 = Existe un registro con el mismo nombre
    def insertarRolOpcion(self, RolOpcion_param):
        resultado = -1
        try:
            #if self.dUserRol.validarIdUnico(RolOpcion_param):
                #resultado = 2
                #return resultado

            if self.dRolOpcion.insertarRolOpcion(RolOpcion_param):
                resultado = 1
            return resultado
        except Exception as e:
            print("Negocio: Error en insertarRolOpcion()", e)

    def eliminarRolOpcion(self, RolOpcion_param):
        resultado = False
        try:
            if self.dRolOpcion.eliminarRolOpcion(RolOpcion_param):
                resultado = True
            return resultado
        except Exception as e:
            print("Negocio: Error en eliminarRolOpcion()", e)
