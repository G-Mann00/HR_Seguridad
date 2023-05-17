import copy


class Country:
    def __init__(self, country_id=None, country_name=None, region_id=None):
        self._country_id = country_id
        self._country_name = country_name
        self._region_id = region_id


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

    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        self._region_id = region_id

    def __str__(self):
        return f'country_id:{self._country_id},country_name:{self._country_name}'

    def __getitem__(self):
        u = copy.copy(self)
        return u
