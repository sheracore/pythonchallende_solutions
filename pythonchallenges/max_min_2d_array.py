# Maybe it could be develped by numpy but i didn't have enough experience
import random

array_2d = list()
# Generating 2d_array
for i in range(4):
    array_2d.append([random.random() for i in range(2)])

print(array_2d)

def max_min_2d_array(array_2d):
    result = list()
    for row in array_2d:
        result.append(max(row))

    return {"row max's": result, "final_max": max(result)}

print(max_min_2d_array(array_2d))
