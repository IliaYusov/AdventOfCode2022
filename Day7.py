path = '/'
files = {}

with open('input.txt') as f:

  for line in f: # собираем словарь суммарных размеров файлов в папках и подпапках
    command = line.strip().split()
    if command[0:2] == ['$', 'cd']:
      if command[2] == '..':
        path = path[:path.rfind('.')]
      elif command[2] == '/':
        pass
      else:
        path += f'.{command[2]}'
    elif command[0].isnumeric():
      path_list = path.split('.')
      for i in range(1, len(path_list) + 1):
        path_rec = '.'.join(path_list[:i])
        files[path_rec] = files.setdefault(path_rec, 0) + int(command[0])

print(sum(size for size in files.values() if size <= 100000))

print(min(size for size in files.values() if size >= files['/'] - 40000000))
