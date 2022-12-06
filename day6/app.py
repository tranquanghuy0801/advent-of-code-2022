f = open('input.txt', "r")
string = f.readline()
string = string.replace("\n", "")
n = len(string)
# num_distinct = 4
num_distinct = 14
start = 0
end = start + num_distinct
while end <= n:
  sub = string[start:end]
  obj = {}
  for char in sub:
    obj[char] = 1
  print(obj)
  if len(obj.keys()) == num_distinct:
    break
  start += 1
  end += 1
print(end)