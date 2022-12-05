arr1 = ['N', 'R', 'G', 'P']
arr2 = ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C']
arr3 = ['M', 'S', 'V']
arr4 = ['L', 'S', 'R', 'C', 'Z', 'P']
arr5 = ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q']
arr6 = ['C', 'T', 'N', 'W', 'D', 'M', 'S']
arr7 = ['H', 'D', 'G', 'W', 'P']
arr8 = ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V']
arr9 = ['R', 'P', 'F', 'L', 'W', 'G', 'Z']
total_arr = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9];
dict_arr = {}
for i in range(9):
  dict_arr[i + 1] = total_arr[i]
f = open('input.txt', "r")
final_str = ''
# for line in f.readlines():
#   line = line.replace("\n", "")
#   options = line.split(" ")
#   num_cranes = int(options[1])
#   start =  int(options[3])
#   end =  int(options[5])
#   for i in range(num_cranes):
#     move_item = dict_arr[start].pop()
#     dict_arr[end].append(move_item)
for line in f.readlines():
  line = line.replace("\n", "")
  options = line.split(" ")
  num_cranes = int(options[1])
  start =  int(options[3])
  end =  int(options[5])
  arr_temp = []
  for i in range(num_cranes):
    move_item = dict_arr[start].pop()
    arr_temp.append(move_item)
  for e in range(len(arr_temp)):
    item = arr_temp.pop()
    dict_arr[end].append(item)
for arr in total_arr:
  final_str += arr[-1]
print(final_str)