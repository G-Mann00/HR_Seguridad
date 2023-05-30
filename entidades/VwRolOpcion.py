import copy

class VwRolOpcion:
    def __init__(self, id_RolOpcion=None, id_rol=None, rol=None,
                id_opcion=None, opcion=None, estado=None):

        self._id_RolOpcion = id_RolOpcion
        self._id_rol = id_rol
        self._rol = rol
        self._id_opcion = id_opcion
        self._opcion = opcion
        self._estado = estado

    def __str__(self):
        return f'''
        id_RolOpcion: {self._id_RolOpcion},
        id_rol: {self._id_rol},
        rol: {self._rol},
        id_opcion: {self._id_opcion},
        opcion: {self._opcion},
        estado: {self._estado},
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        return u

    @property
    def id_RolOpcion(self):
        return self._id_RolOpcion

    # SET
    @id_RolOpcion.setter
    def id_RolOpcion(self, id_RolOpcion):
        self._id_RolOpcion = id_RolOpcion

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

    @property
    def id_opcion(self):
        return self._id_opcion

    @id_opcion.setter
    def id_opcion(self, id_opcion):
        self._id_opcion = id_opcion

    @property
    def opcion(self):
        return self._opcion

    @opcion.setter
    def opcion(self, opcion):
        self._opcion = opcion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado