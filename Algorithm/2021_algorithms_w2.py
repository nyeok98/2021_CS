"""
랜덤으로 수 생성
"""
import random

my_counter = dict() # dictionary has key-value pair

for i in range(10):
    r = random.randint(0, 4)
    if r in my_counter.keys():
        my_counter[r] = my_counter[r] + 1
    else:
        my_counter[r] = 1

"""
표 그리기
"""
import matplotlib.pyplot as plt
plt.bar(my_counter.keys(), my_counter.values())

"""
Knuth Shuffle
"""

a = [1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
    r = random.randint(i, len(a)-1)
    a[i], a[r] = a[r], a[i]

print(a)

