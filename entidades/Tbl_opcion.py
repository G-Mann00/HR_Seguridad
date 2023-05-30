import copy

class Tbl_opcion:
    def __init__(self, id_opcion=None, opcion=None, estado=None):

        self._id_opcion = id_opcion
        self._opcion = opcion
        self._estado = estado

    def __str__(self):
        return f'''
    
        id_opcion: {self._id_opcion},
        opcion: {self._opcion},
        estado: {self._estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)

        u.id_opcion = u._id_opcion
        u.opcion = u._opcion
        u.estado = u._estado

        return u

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
        return self.estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado