class VwCountries:

    def __init__(self, country_id=None, country_name=None, region_name=None):
        self._country_id = country_id
        self._country_name = country_name
        self._region_name = region_name

    @property
    def country_id(self):
        return self._country_id

    @property
    def country_name(self):
        return self._country_name

    @property
    def region_name(self):
        return self._region_name

    @country_id.setter
    def country_id(self, country_id):
        self._country_id = country_id

    @country_name.setter
    def country_name(self, country_name):
        self._country_name = country_name

    @region_name.setter
    def region_name(self, region_name):
        self._region_name = region_name


