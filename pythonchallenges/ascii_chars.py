import string
import random

def sum_ascii_coods(random_string):
    sum_ = 0 
    print(random_string)
    for letter in random_string:
        sum_ += ord(letter)

    return sum_

all_strings = string.ascii_letters + string.digits + string.punctuation
random_length = random.randrange(5,15)
random_string = ''.join(random.choice(all_strings) for _ in range(random_length))


print(sum_ascii_coods(random_string))
