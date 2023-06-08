class VwEmployees:
    
    def __init__(self, employee_id=None, first_name=None, last_name=None, email=None, 
                  phone_number=None, hire_date=None, job=None, salary=None, manager=None, department=None):
         self._employee_id = employee_id
         self._first_name = first_name
         self._last_name = last_name
         self._email = email
         self._phone_number = phone_number
         self._hire_date = hire_date
         self._job = job
         self._salary = salary
         self._manager = manager
         self._department = department
    
    @property
    def employee_id(self):
        return self._employee_id
    
    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number
    
    @property
    def hire_date(self):
        return self._hire_date
    
    @hire_date.setter
    def hire_date(self, hire_date):
        self._hire_date = hire_date
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job):
        self._job = job
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        self._salary = salary
    
    @property
    def manager(self):
        return self._manager
    
    @manager.setter
    def manager(self, manager):
        self._manager = manager
    
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, department):
        self._department = department
    