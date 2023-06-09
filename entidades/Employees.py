import copy

class Employees:
    def __init__(self, employee_id=None, first_name=None, last_name=None, email=None, phone_number=None, hire_date=None, 
                       job_id=None, salary=None, manager_id=None, department_id=None):
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self._hire_date = hire_date
        self._job_id = job_id
        self._salary = salary
        self._manager_id = manager_id
        self._department_id = department_id
    
    def __str__(self):
        return f'''
        employee_id: {self._employee_id},
        first_name: {self._first_name},
        last_name: {self._last_name},
        email: {self._email},
        phone_number: {self._phone_number},
        hire_date: {self._hire_date},
        job_id: {self._job_id},
        salary: {self._salary},
        manager_id: {self._manager_id},
        deparment_id: {self._deparment_id}
        '''
    
    def __getitem__(self):
        u = copy.copy(self)
        return u
    
    
    'Getters y Setters'

    'employee_id'
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id
        
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
        
    'email'
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
    
    'phone_number'
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number
    
    'hire_date'
    @property
    def hire_date(self):
        return self._hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self._hire_date = hire_date
    
    'job_id'
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        self._job_id = job_id
    
    'salary'
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary
    
    'manager_id'
    @property
    def manager_id(self):
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        self._manager_id = manager_id
    
    'department_id'
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        self._department_id = department_id
