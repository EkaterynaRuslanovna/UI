import random

"""
Generating random person data for add customer.
"""


def generated_person_data():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis']
    post_codes = ['10001', '20002', '30003', '40004', '50005']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    post_code = random.choice(post_codes)

    return first_name, last_name, post_code
