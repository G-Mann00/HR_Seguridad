import copy


class VwRol:
    def __init__(self, id_rol=None, rol=None, estado=None):
        self._id_rol = id_rol
        self._rol = rol

    def __str__(self):
        return f'''

        id_rol: {self._id_rol},
        rol: {self._rol},
        '''

    def __getitem__(self, item):
        u = copy.copy(self)

        u.id_rol = u._id_rol
        u.rol = u._rol
        return u

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
