list_ = list(range(1,11))
print(list_)

for index in range(len(list_)-1):
    if index%2 != 0: continue
    tmp = list_[index]
    list_[index] = list_[index+1]
    list_[index+1] = tmp

print(list_)
