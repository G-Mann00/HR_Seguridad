import copy


class Jobs:
    def __init__(self, job_id=None, job_title=None, min_salary=None, max_salary=None):
        self._job_id = job_id
        self._job_title = job_title
        self._min_salary = min_salary
        self._max_salary = max_salary

    def __str__(self):
        return f'job_id:{self._job_id},job_title:{self._job_title},min_salary:{self._min_salary},max_salary:{self._max_salary}'

    def __getitem__(self):
        u = copy.copy(self)
        return u


    'Getters y Setters'
    'job_id'
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        self._job_id = job_id
    
    'job_title'
    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        self._job_title = job_title
    
    'min_salary'
    @property
    def min_salary(self):
        return self._min_salary

    @min_salary.setter
    def min_salary(self, min_salary):
        self._min_salary = min_salary
    
    'max_salary'
    @property
    def max_salary(self):
        return self._max_salary

    @max_salary.setter
    def max_salary(self, max_salary):
        self._max_salary = max_salary
