class Vw_Location:
    def __init__(self, id_department=None, department_name=None, city=None):
        self._id_department = id_department
        self._department_name = department_name
        self._city = city

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
        self._department_name = department_name

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city
