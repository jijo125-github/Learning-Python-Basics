import logging

logging.basicConfig(
    filename='Code/Logging/Basics/emp.log',
    level=logging.INFO, 
    format='%(levelname)s:%(message)s'
)

class Employee:
    """ Sample Employee class """

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        logging.info(f'Created Employee:{self.fullname}|{self.emailid}')

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def emailid(self):
        return f'{self.firstname}@gmail.com'


emp1 = Employee(fname='Jijo', lname='Johns')
emp2 = Employee(fname='Marsh', lname='Robins')
