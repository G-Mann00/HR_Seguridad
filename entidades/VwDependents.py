class VwDependents:
    def __init__(self, dependent_id=None, first_name=None, last_name=None, relationship=None, employee_name=None):
        self._dependent_id = dependent_id
        self._first_name = first_name
        self._last_name = last_name
        self._relationship = relationship
        self._employee_name = employee_name

    'dependent_id'

    @property
    def dependent_id(self):
        return self._dependent_id

    @dependent_id.setter
    def dependent_id(self, dependent_id):
        self.dependent_id = dependent_id

    'first_name'

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self.first_name = first_name

    'last_name'

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self.last_name = last_name

    'relationship'

    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        self.relationship = relationship

    'employee_name'

    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, employee_name):
        self.employee_name = employee_name
