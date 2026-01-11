import random
import re
nums = [random.randint(1,9) for i in range(4)]
print(nums)
equation = input()
used_nums = list(map(int, re.findall(r'\d+', equation)))
temp = nums.copy()
valid = True
for num in used_nums:
    if num in temp:
        temp.remove(num)
    else:
        valid = False
        break
if not valid:
    print("wrong input")
else:
    result = eval(equation)
    if result == 24:
        print("correct")
    else:
        print("incorrect")