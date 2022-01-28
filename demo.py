import random

def generate(num = 100):
    dict = {}
    for i in range(num):
        contact = random.randint(1000000000, 9999999999)
        contacts = {}
        for j in range(100):
            contacts[j] = []
        for j in range(num):
            number = random.randint(1000000000, 9999999999)
            contacts[number // 100000000].append(number)
        dict[contact] = contacts
    return dict

print(generate())
