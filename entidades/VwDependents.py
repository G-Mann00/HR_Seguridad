class VwDependents:
    def __init__(self, dependent_id = None, first_name = None, last_name = None, relationship = None, employee_name = None):
        self._dependent_id = dependent_id
        self._first_name = first_name
        self._last_name = last_name
        self._relationship = relationship
        self._employee_name = employee_name

    'dependent_id'
    @property
    def dependent_id(self):
        return self._dependent_id

    'first_name'
    @property
    def first_name(self):
        return self._first_name

    'last_name'
    @property
    def last_name(self):
        return self._last_name

    'relationship'
    def relationship(self):
        return self._relationship

    'employee_name'
    def employee_name(self):
        return self._employee_name
