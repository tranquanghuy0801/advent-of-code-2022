f = open('input.txt', "r")
map = []
for line in f.readlines():
  line = line.replace("\n", "")
  row = [int(x) for x in line]
  map.append(row)
num_row = len(map)
num_col = len(map[0])
map_inv = []
for i in range(num_col):
  element = []
  for j in range(num_row):
    element.append(map[j][i])
  map_inv.append(element)

total_count = 0
# total_count += (num_row * 2 + num_col * 2 - 4)

# Part 1
# for i in range(1, num_row - 1):
#   for j in range(1, num_col - 1):
#     val = map[i][j]
#     row = map[i]
#     col = map_inv[j]
#     left_visible = True
#     right_visible = True
#     top_visible = True
#     down_visible = True
#     total_left = 0
#     for left in row[:j]:
#       if left >= val:
#         left_visible = False
#         break
#     for right in row[j+1:]:
#       if right >= val:
#         right_visible = False
#         break
#     for top in col[:i]:
#       if top >= val:
#         top_visible = False
#         break
#     for down in col[i+1:]:
#       if down >= val:
#         down_visible = False
#         break
#     if top_visible or down_visible or right_visible or left_visible:
#       print(val, i, j)
#       print(row[:i],map[i][j],row[i+1:])
#       total_count += 1

# Part 2
for i in range(1, num_row - 1):
  for j in range(1, num_col - 1):
    val = map[i][j]
    row = map[i]
    col = map_inv[j]
    left_count = 0
    right_count = 0
    top_count = 0
    down_count = 0
    for left in list(reversed(row[:j])):
      left_count += 1
      if left >= val:
        break
    for right in row[j+1:]:
      right_count += 1
      if right >= val:
        break
    for top in list(reversed(col[:i])):
      top_count += 1
      if top >= val:
        break
    for down in col[i+1:]:
      down_count += 1
      if down >= val:
        break
    total_count = max(total_count, left_count * right_count * top_count * down_count)
print(total_count)