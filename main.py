import lock
from data import data

# create lock
lock = lock.Lock()

# split data to individual strings in list
new_data = data.split()

# check through data
for number in new_data:
    lock.turn(number)

# print amount of zeros
print(f"The answer is {lock.zeros}")


