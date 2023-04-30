import copy


class Country:
    def __init__(self, country_id=None, country_name=None):
        self._country_id = country_id
        self._country_name = country_name

    @property
    def country_id(self):
        return self._country_id

    @property
    def country_name(self):
        return self._country_name

    @country_id.setter
    def country_id(self, country_id):
        self._country_id = country_id

    @country_name.setter
    def country_name(self, country_name):
        self._country_name = country_name

    def __str__(self):
        return f'country_id:{self._country_id},country_name:{self._country_name}'

    def __getitem__(self):
        u = copy.copy(self)
        return u
