import copy

class Departments:
    def __init__(self, id_department=None, department_name=None, location=None):

        self._id_department=id_department
        self._department_name=department_name
        self._location=location

    def __str__(self):
        return f'''
        id_department= {self._id_department}
        department_name= {self._department_name}
        location= {self._location}
        '''
    def __getitem__(self, item):
        u=copy.copy()

        u.id_department=u._id_department
        u.department_name=u.department_name
        u.location=u.location
        return u

    @property
    def id_department(self):
        return self._id_department

    @id_department.setter
    def id_department(self, id_department):
        self._id_department = id_department

    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        self._department_name=department_name

    @property
    def location(self):
        return self._location

    @location.setter
    def user(self, location):
        self._location = location



