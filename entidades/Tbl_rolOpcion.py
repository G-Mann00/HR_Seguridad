import copy


class Tbl_rolOpcion:

    def __init__(self, id_rolOpcion=None, id_rol=None, id_opcion=None):
        self._id_rolOpcion = id_rolOpcion
        self._id_rol = id_rol
        self._id_opcion = id_opcion

    def __str__(self):
        return f'''
        id_rolOpcion: {self._id_rolOpcion},
        id_rol: {self._id_rol},
        id_opcion: {self._id_opcion}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.id_rolOpcion = u._id_rolOpcion
        u.id_rol = u._id_rol
        u.id_opcion = u._id_opcion
        return u

    # GET & SET

    @property
    def id_rolOpcion(self):
        return self._id_opcion

    @id_rolOpcion.setter
    def id_rolOpcion(self, id_rolOpcion):
        self._id_rolOpcion = id_rolOpcion

    @property
    def id_rol(self):
        return self._id_rol

    @id_rol.setter
    def id_rol(self, id_rol):
        self._id_rol = id_rol

    @property
    def id_opcion(self):
        return self._id_opcion

    @id_opcion.setter
    def id_opcion(self, id_opcion):
        self._id_opcion = id_opcion
