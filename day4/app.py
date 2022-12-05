total_contains = 0
f = open('input.txt', "r")
for line in f.readlines():
  line = line.replace("\n", "")
  first, second = line.split(',')
  first_start, first_last = [int(e) for e in first.split('-')]
  second_start, second_last = [int(e) for e in second.split('-')]
  # if (int(first_start) <= int(second_start) and int(second_last) <= int(first_last)) or \
  #   (int(second_start) <= int(first_start) and int(first_last) <= int(second_last)):
  #   total_contains += 1
  if (second_start >= first_start and second_start <= first_last) or (first_start >= second_start and first_start <= second_last):
    total_contains += 1
print(total_contains)