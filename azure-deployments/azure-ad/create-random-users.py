from os import system as cs
from random import randint

cs('pip install names')
import names, string, secrets

class basic_info:
    
    def generate_password(self, length=randint(10, 16)):
        # Define characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate random password
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password
    
    def __init__(self) -> None:
        self.first_name = names.get_first_name() # First Name
        self.last_name = names.get_last_name() # Last Name
        self.display_name = self.first_name + " " + self.last_name
        self.email = self.first_name.lower() + self.last_name.lower() + "@tfslabs.onmicrosoft.com"
        self.password = self.generate_password()
        self.basic_info = [self.first_name, self.last_name, self.display_name, self.email, self.password]

class employment_info:
    
    
    def job_title(self):
        roles = [
            ['Captain', 'First Officer', 'Second Officer', 'Flight Attendant'],
            ['Check-in Personel', 'Customer Service'],
            ['Inspector', 'Maintainer'],
            ['Flight Scheduling Manager', 'Payload Manager'],
            ['Finance Operator', 'Human Resources', 'Advertisement Manager']
        ]
        flight_attendants = roles[0][randint(0, 3)]
        customer_checkin = roles[1][randint(0, 1)]
        maintenance_crew = roles[2][randint(0, 1)]
        flight_manager = roles[3][randint(0, 1)]
        administrative_role = roles[4][randint(0, 2)]
    
    def __init__(self) -> None:
        pass 