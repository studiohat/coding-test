arr = [0,1,0,2,1,0,1,3,2,1,2,1]

if not arr:
    print(0)

rst = 0

left, right = 0, len(arr)-1

left_max, right_max = arr[left], arr[right]

while left < right:
    left_max, right_max = max(left_max, arr[left]), max(right_max, arr[right])

    if left_max <= right_max:
        rst += left_max - arr[left]
        left += 1
    else:
        rst += right_max - arr[right]
        right -= 1
    
print(rst)