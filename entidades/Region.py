import copy


class Region:
    def __init__(self, region_id=None, region_name=None):
        self._region_id = region_id
        self._region_name = region_name

    @property
    def region_id(self):
        return self._region_id

    @property
    def region_name(self):
        return self._region_name

    @region_id.setter
    def region_id(self, region_id):
        self._region_id = region_id

    @region_name.setter
    def region_name(self, region_name):
        self._region_name = region_name

    # Este metodo no es adecuado. Preguntar al profesor
    def __getitem__(self):
        u = copy.copy(self)
        return u

    def __str__(self):
        return f'region_id:{self.region_id},region_name:{self.region_name}'