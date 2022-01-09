import json
from faker import Faker

fake = Faker()

def generate_data(): 
        
        """
        This is to generate data that will be 
        used in create new admin user
        """

        data = {}
        data['data'] = []
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        address1 = fake.address()
        address2 = fake.address()
        phone = fake.phone_number()
        country = fake.country()
        data['data'].append({'first_name': first_name, 
                                'last_name': last_name,
                                'email': email,
                                'address1': address1,
                                'address2': address2,
                                'phone': phone,
                                'country': country})
        with open('generated_data.json', 'w') as gd:
            json.dump(data, gd)
        return data

generate_data()
