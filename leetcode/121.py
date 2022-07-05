#카데인 알고리즘

import sys

prices = [7,1,5,3,6,4]

profit = 0
min_price = sys.maxsize

for i in prices:
    min_price = min(min_price, i)
    profit = max(profit, i-min_price)

print(profit)