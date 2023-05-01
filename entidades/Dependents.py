import copy

class Dependents:
    def __init__(self, dependent_id=None, first_name=None, last_name=None, relationship=None, employee_id=None):
        self._dependent_id = dependent_id
        self._first_name = first_name
        self._last_name = last_name
        self._relationship = relationship
        self._employee_id = employee_id
    
    def __str__(self):
        return f'''
        dependent_id: {self._dependent_id},
        first_name: {self._first_name},
        last_name: {self._last_name},
        relationship: {self._relationship},
        employee_id: {self._employee_id}
        '''
    
    def __getitem__(self):
        u = copy.copy(self)
        return u
    
    
    'Getters y Setters'

    'dependent_id'
    @property
    def dependent_id(self):
        return self._dependent_id

    @dependent_id.setter
    def dependent_id(self, dependent_id):
        self._dependent_id = dependent_id
    
    'first_name'
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    
    'last_name'
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    'relationship'
    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        self._relationship = relationship
    
    'employee_id'
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id