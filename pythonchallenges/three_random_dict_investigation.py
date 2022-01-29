import string
import random

from collections import Counter

def generate_dict():
    random_100 = random.randint(0,100)
    letters = string.ascii_letters

    my_dict = dict()
    for i in range(random_100):
        random_10 = random.randint(0,10)
        random_1_10 = random.randint(1,10)
        key_ = ''.join(random.sample(string.ascii_letters, random_1_10))
        my_dict[key_] = random_10

    return my_dict

my_dict = generate_dict()
print(my_dict)

print("\n1 :", Counter(my_dict.values()))

max_value =  max(my_dict.values())
max_ = list(my_dict.keys())[list(my_dict.values()).index(max_value)]
print("2 :", max_)

filter_ = list(filter(lambda x:  3<=len(x)<=5, my_dict.keys()))
print("3 :", filter_)
