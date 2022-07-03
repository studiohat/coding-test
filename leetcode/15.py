import time
from itertools import combinations

start_time = time.process_time()
nums = [-1,0, 1, 2, -1 , -4]

nums.sort()

rst = []

a = combinations(nums,3)

a = list(set(a))


for i in a:
    if sum(i) == 0:
        rst.append(i)

print(rst)

end_time = time.process_time()
print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")