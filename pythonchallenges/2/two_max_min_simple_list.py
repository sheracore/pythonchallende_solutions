import random

# Generating random list solution 1
random_list = [random.random() for _ in range(100)]
# Generating random list solution 2
random_list = random.sample(range(0, 100000), 5)

# soulotion 1
print(max(random_list))
print(min(random_list))

# soulotion 2

def max_min(random_list):
    max_, min_ = None, None
    for value in random_list:
        if not max_ : max_ = value
        if not min_ : min_ = value
        if value > max_:
            max_ = value
        elif value < min_:
            min_ = value

    return  {'max': max_, "min": min_}

print(max_min(random_list))
