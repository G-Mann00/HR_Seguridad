import copy


class Location:
    def __init__(self, location_id=None, street_address=None, postal_code=None, city=None, state_province=None, country_id=None):
        self._location_id = location_id
        self._street_address = street_address
        self._postal_code = postal_code
        self._city = city
        self._state_province = state_province
        self._country_id = country_id

    @property
    def location_id(self):
        return self._location_id

    @property
    def street_address(self):
        return self._street_address

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def city(self):
        return self._city

    @property
    def state_province(self):
        return self._state_province

    @property
    def country_id(self):
        return self._country_id

    @location_id.setter
    def location_id(self, location_id):
        self._location_id = location_id

    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    @city.setter
    def city(self, city):
        self._city = city

    @state_province.setter
    def state_province(self, state_province):
        self._state_province = state_province

    @country_id.setter
    def country_id(self, country_id):
        self._country_id = country_id

    def __str__(self):
        return f"location_id:{self._location_id}" \
               f",street_address:{self._street_address}" \
               f",postal_code:{self._postal_code}" \
               f",city:{self._city}" \
               f",state_province:{self._state_province}" \
               f",country_id:{self._country_id}"

    def __getitem__(self):
        u = copy.copy(self)
        return u

