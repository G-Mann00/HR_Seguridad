from datos.Dt_tbl_rol import Dt_tbl_rol
from entidades.Tbl_rol import Tbl_rol

class Ng_Rol:
    def __init__(self):
        self.rol = Tbl_rol()
    dr = Dt_tbl_rol()

    def validarNombre(self, rol, rol_id=None):
        roles = self.dr.listarRol()
        if rol_id is None:
            for r in roles:
                if r.rol == rol.rol:
                    return False
        else:
            for r in roles:
                if r.id_rol == rol_id and r.rol == rol.rol:
                    return False
        return True

    def agregarRol(self, rol):
        if not self.validarNombre(rol):
            return False
        self.dr.agregarRol(rol)

    def modificarRol(self, rol, id_rol):
        if not self.validarNombre(rol, id_rol):
            return False
        self.dr.editarRol(rol)