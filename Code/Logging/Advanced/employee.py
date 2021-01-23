import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

filehandler = logging.FileHandler(filename='Code/Logging/Advanced/employee.log')
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

class Employee:
    """ Sample Employee class """

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        logger.info(f'Created Employee:{self.fullname}|{self.emailid}')

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def emailid(self):
        return f'{self.firstname}@gmail.com'


emp1 = Employee(fname='Jijo', lname='Johns')
emp2 = Employee(fname='Marsh', lname='Robins')
