f = open('input.txt', "r")
history = {'root': {}}
curr_dir = ['root']
def get_dict_path(d: dict, path: list) -> dict:
    if len(path) == 1:
        return d[path[0]]
    else:
        return get_dict_path(d[path[0]], path[1:])

for line in f.readlines():
  line = line.replace("\n", "")
  if "$ ls" in line:
    continue
  if "$ cd" in line:
    command = line.replace("$ cd", "").strip()
    if command == "..":
      curr_dir.pop()
    elif command != "/":
      curr_dir.append(command)
  else:
    marker, name = line.split()
    print(marker, name)
    if marker.isnumeric():
      get_dict_path(history, curr_dir)[name] = int(marker)
    else:
      get_dict_path(history, curr_dir)[name] = {}

def directory_size(d: dict) -> int:
    return sum(directory_size(v) if isinstance(v, dict) else v for v in d.values())

def traverse_dict(d: dict, res=None) -> None:
    if not res:
        res = []

    for k, v in d.items():
        if not isinstance(v, dict):
            continue
        res.append(directory_size(v))
        traverse_dict(v, res)
    
    return res

print(history)
directory_sizes = traverse_dict(history)
# Part 1
print(sum(n for n in directory_sizes if n <= 100000))
# Part 2
max_size = max(directory_sizes)
unused = 70000000 - max_size
available = 30000000 - unused
print(min(n for n in directory_sizes if n >= available))

