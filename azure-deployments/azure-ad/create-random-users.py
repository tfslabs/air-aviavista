from os import system as cs
from random import randint

cs('pip install names')
import names, string, secrets

class EmploymentInfo:
    def __init__(self):
        self.department_number = randint(0, 4)
        self.department, self.departmentCode = self._get_department(self.department_number)

        if self.department_number == 0:
            role_position = randint(0, 3)
            self.job_title = self._get_job_title(0, role_position)
        elif self.department_number == 1:
            role_position = randint(0, 2)
            self.job_title = self._get_job_title(1, role_position)
        else:
            role_position = randint(0, 1)
            self.job_title = self._get_job_title(self.department_number, role_position)

        self.usage_location_number = randint(0, 2)
        self.usage_location = self._get_usage_location(self.usage_location_number)

        if self.usage_location_number == 0:
            self.city = self._get_city(0, randint(0, 3))
        else:
            self.city = self._get_city(self.usage_location_number, 0)
        
        
        self.first_name = names.get_first_name() # First Name
        self.last_name = names.get_last_name() # Last Name
        self.display_name = self.first_name + " " + self.last_name
        self.email = self.first_name.lower() + self.last_name.lower() + '__' + self.departmentCode + "@airaviavista.onmicrosoft.com"
        self.password = self.generate_password()
        self.accountEnable = "Yes"
        
        self.employment_info = [
            self.display_name,   #1
            self.email,          #2
            self.password,       #3
            self.accountEnable,  #4
            self.first_name,     #5
            self.last_name,      #6
            self.job_title,      #7
            self.department,     #8
            self.usage_location, #9
            '',                  #10
            '',                  #11
            self.usage_location, #12
            '',                  #13
            self.city,           #14
            '',                  #15
            '',                  #16
            ''                   #17
        ]

    def _get_department(self, department_number):
        departments = [
            'In-Flight Department',
            'Administrative Department',
            'Customer Services Department',
            'Maintenance Department',
            'Scheduling and Safety Department'
        ]
        departmentCode = [
            'IFD',
            'ADe',
            'CSD',
            'MDe',
            'SSDe'
        ]
        return departments[department_number], departmentCode[department_number]

    def _get_job_title(self, department_number, role_number):
        roles = [
            ['Captain', 'First Officer', 'Second Officer', 'Flight Attendant'],  # In-Flight Department
            ['Finance Operator', 'Human Resources', 'Advertisement Manager'],  # Administrative Department
            ['Check-in Personnel', 'Customer Service'],  # Customer Services Department
            ['Inspector', 'Maintainer'],  # Maintenance Department
            ['Flight Scheduling Manager', 'Payload Manager']  # Scheduling and Safety Department
        ]
        return roles[department_number][role_number]

    def _get_usage_location(self, country_number):
        countries = [
            'United States',
            'United Kingdom',
            'France'
        ]
        return countries[country_number]

    def _get_city(self, country_number, city_index):
        cities = [
            ['Miami', 'Boston', 'San Francisco', 'Broward County'],  # US
            ['London'],  # UK
            ['Paris']  # France
        ]
        return cities[country_number][city_index]

    def generate_password(self, length=randint(10, 16)):
        characters = string.ascii_letters + string.digits + '@_+=<>'
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

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

def append_array_to_file(array):
    with open('UserCreateTemplate.csv', 'a') as file:
        file.write('\n')
        for element in array:
            file.write(str(element) + ',')

get_user_input = int(input("How many user you want to create?: "))

with open('UserCreateTemplate.csv', 'a') as file:
    file.write('version:v1.0,,,,,,,,,,,,,,,,\n')
    file.write('Name [displayName] Required,User name [userPrincipalName] Required,Initial password [passwordProfile] Required,Block sign in (Yes/No) [accountEnabled] Required,First name [givenName],Last name [surname],Job title [jobTitle],Department [department],Usage location [usageLocation],Street address [streetAddress],State or province [state],Country or region [country],Office [physicalDeliveryOfficeName],City [city],ZIP or postal code [postalCode],Office phone [telephoneNumber],Mobile phone [mobile]')

for i in range(0, get_user_input + 1):
    employee_info = EmploymentInfo().employment_info
    append_array_to_file(employee_info)