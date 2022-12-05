total_priority = 0
f = open('input.txt', "r")
# for line in f.readlines():
#   line = line.replace("\n", "")
#   index = len(line) // 2
#   first_half = line[:index]
#   second_half = line[index:]
#   obj = {}
#   for char in first_half:
#     if char not in obj:
#       obj[char] = 1
#   common_char = ''
#   for char in second_half:
#     if char in obj:
#       common_char = char
#   if common_char.islower():
#     total_priority += (ord(common_char) - 96)
#   else:
#     total_priority += (ord(common_char) - 38)
lines = f.readlines()
for i in range(0, len(lines), 3):
  group = lines[i:i+3]
  first, second, third = group[0], group[1], group[2]
  first = first.replace("\n", "")
  second = second.replace("\n", "")
  third = third.replace("\n", "")
  obj = {}
  common_char = ''
  # print(first,'-', second, '-', third)
  for char in first:
    if char not in obj:
      obj[char] = 1
  for char in second:
    if char in obj:
      obj[char] = 2
  for char in third:
    if char in obj and obj[char] == 2:
      common_char = char
  if common_char.islower():
    total_priority += (ord(common_char) - 96)
  else:
    total_priority += (ord(common_char) - 38)

print(total_priority)