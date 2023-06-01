import copy

class VwGestionUsuario:
    def __init__(self, id_user=None, user=None, pwd=None,
                nombres=None, apellidos=None, email=None):

        self._id_user=id_user
        self._user=user
        self._pwd=pwd
        self._nombres=nombres
        self._apellidos=apellidos
        self._email=email

    def __str__(self):
        return f'''
        iduser: {self._id_user},
        user: {self._user},
        pwd: {self._pwd},
        nombres: {self._nombres},
        apellidos: {self._apellidos},
        email: {self._email},
        '''
    def __getitem__(self, item):
        u=copy.copy(self)

        u.id_user=u._id_user
        u.user=u._user
        u.pwd=u._pwd
        u.nombres=u.nombres
        u.apellidos=u._apellidos
        u.email=u._email

        return u

        # GET
        @property
        def id_user(self):
            return self._id_user

        # SET
        @id_user.setter
        def id_user(self, id_user):
            self._id_user = id_user

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
        def user(self):
            return self._user

        @user.setter
        def user(self, user):
            self._user = user

        @property
        def pwd(self):
            return self._pwd

        @pwd.setter
        def pwd(self, pwd):
            self._pwd = pwd

        @property
        def email(self):
            return self._email

        @email
        def email(self, email):
            self._email = email