import re

f = open('input.txt', "r")
max_calories = 0
curr_calories = 0
arr = []
for line in f.readlines():
  num = re.sub('\D', '', line)
  if num == "":
    arr.append(curr_calories)
    max_calories = max(max_calories, curr_calories)
    curr_calories = 0
    continue
  curr_calories = curr_calories + int(num)

arr.sort()

print(max_calories)
print(arr)
print(sum(arr[-3:]))