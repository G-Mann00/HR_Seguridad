import copy

class VwUserRol:
    def __init__(self, id_UserRol=None,  id_user=None, user=None, pwd=None,
                 nombres=None, apellidos=None, email=None,
                 pwd_temp=None, estado=None, id_rol=None, rol=None):
        self._idUserRol = id_UserRol
        self._id_user = id_user
        self._user = user
        self._pwd = pwd
        self._nombres = nombres
        self._apellidos = apellidos
        self._email = email
        self._pwd_temp = pwd_temp
        self._estado = estado
        self._id_rol = id_rol
        self._rol = rol

    def __str__(self):
        return f'''
        id_UserRol: {self._idUserRol},
        id_user: {self._id_user},
        user: {self._user},
        pwd: {self._pwd},
        nombres: {self._nombres},
        apellidos: {self._apellidos},
        email: {self._email},
        pwd_temp: {self._pwd_temp},
        estado: {self._estado},
        id_rol: {self._id_rol},
        rol: {self._rol}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        return u

    # GET

    @property
    def id_UserRol(self):
        return self._idUserRol

    # SET
    @id_UserRol.setter
    def id_UserRol(self, id_UserRol):
        self._id_UserRol = id_UserRol
    @property
    def id_user(self):
        return self._id_user

    # SET
    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, nombres):
        self._nombres = nombres

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        self._pwd = pwd

    @property
    def pwd_temp(self):
        return self._pwd_temp

    @pwd_temp.setter
    def pwd_temp(self, pwd_temp):
        self._pwd_temp = pwd_temp

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

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
