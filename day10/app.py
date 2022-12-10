def calc_cycle(num_cycle, register):
  marks = 0
  if num_cycle == 20:
    marks += 20 * register
  elif num_cycle == 60:
    marks += 60 * register
  elif num_cycle == 100:
    marks += 100 * register
  elif num_cycle == 140:
    marks += 140 * register
  elif num_cycle == 180:
    marks += 180 * register
  elif num_cycle == 220:
    marks += 220 * register
  return marks

f = open('input.txt', "r")
# Part 1
# num_cycle = 0
# total_marks = 0
# register = 1
# for line in f.readlines():
#   line = line.replace("\n", "")
#   if line == 'noop':
#     num_cycle += 1
#     total_marks += calc_cycle(num_cycle + 1, register)
#   else:
#     command, val = line.split()
#     num_cycle += 1
#     total_marks += calc_cycle(num_cycle + 1, register)
#     num_cycle += 1
#     register += int(val)
#     total_marks += calc_cycle(num_cycle + 1, register)
# print(total_marks)

# Part 2
string_draw = ''
register_X = 1
num_cycle = 0
for line in f.readlines():
  line = line.replace("\n", "")
  if line == 'noop':
    num_cycle += 1
    if num_cycle == register_X or num_cycle == register_X + 1 or num_cycle == register_X + 2:
      string_draw += '#'
    else:
      string_draw += '.'
    if num_cycle == 40:
      num_cycle = 0
  else:
      command, val = line.split()
      num_cycle += 1
      if num_cycle == register_X or num_cycle == register_X + 1 or num_cycle == register_X + 2:
        string_draw += '#'
      else:
        string_draw += '.'
      if num_cycle == 40:
        num_cycle = 0
      num_cycle += 1
      if num_cycle == register_X or num_cycle == register_X + 1 or num_cycle == register_X + 2:
        string_draw += '#'
      else:
        string_draw += '.'
      register_X += int(val)
      if num_cycle == 40:
        num_cycle = 0

for i in range(6):
  print(string_draw[i*40:(i+1)*40])

