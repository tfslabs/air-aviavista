from os import system as cs
from random import randint

cs('pip install names')
import names, string, secrets

class basic_info:
    
    def generate_password(self, length=randint(10, 16)):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password
    
    def __init__(self) -> None:
        self.first_name = names.get_first_name() # First Name
        self.last_name = names.get_last_name() # Last Name
        self.display_name = self.first_name + " " + self.last_name
        self.email = self.first_name.lower() + self.last_name.lower() + "@tfslabs.onmicrosoft.com"
        self.password = self.generate_password()
        self.accountEnable = "Yes"
        self.basic_info = [self.display_name, self.email, self.password, self.accountEnable, self.first_name, self.last_name]

class employment_info:
    
    def usageLocation(self, countryNumber):
        country = [
            'United States',
            'United Kingdom',
            'France'
        ]
        return country[countryNumber]
    
    def department(self,department_number):
        departments = [
            'In-Flight Department',
            'Administrative Department',
            'Customer Services Department',
            'Maintaince Department',
            'Scheduling and Safety Department'
        ]
        return departments[department_number]
    
    def job_title(self, department_number, role_number):
        roles = [
            ['Captain', 'First Officer', 'Second Officer', 'Flight Attendant'], # In-Flight Department
            ['Finance Operator', 'Human Resources', 'Advertisement Manager'],   # Administrative Department
            ['Check-in Personel', 'Customer Service'],                          # Customer Services Department
            ['Inspector', 'Maintainer'],                                        # Maintaince Department
            ['Flight Scheduling Manager', 'Payload Manager']                    # Scheduling and Safety Department
        ]
        return roles[department_number][role_number]
    
    def __init__(self):
        self.department_number = randint(0, 4)
        self.department = self.department(self.department_number)
        
        if self.department_number == 0:
            self.jobTitle = self.job_title(0, randint(0, 3))
        elif self.department_number == 1:
            self.jobTitle = self.job_title(1, randint(0, 2))
        else:
            self.jobTitle = self.job_title(self.department_number, randint(0, 1))
        
        self.usageLocationNumber = randint(0, 2)
        self.usageLocation = self.usageLocation(self.usageLocationNumber)

    
employee_info = basic_info().basic_info + employment_info().employment_info
'''
The employee info must be following this format:
<----- Basic Info
1. displayName
2. userPrincipalName
3. passwordProfile
4. accountEnable
5. givenName
6. surname
----->

<------ emplyement_info
7. jobTitle
8. department
9. usageLocation
10. streetAddress
11. state
12. country
13. physicalDeliveryOfficeName
14. city
15. postalCode
16. telephoneNumber
17. mobile
----->
'''