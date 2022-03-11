import collections
from directions import sample_input
import copy

routes = copy.copy(sample_input)

def find_routes(routes):
  edges = collections.defaultdict(set)
  for line in routes.splitlines():
    src, dst = line.split('-')
    edges[src].add(dst)
    edges[dst].add(src)

  all_paths = set()

  todo = [(('start',), False)]
  while todo:
    path, double_cave = todo.pop()

    if path[-1] == 'end':
      all_paths.add(path)
      continue

    for cand in edges[path[-1]]:
      if cand == 'start':
        continue
      elif cand.isupper() or cand not in path:
        todo.append(((*path, cand), double_cave))
      elif not double_cave and path.count(cand) ==1:
        todo.append(((*path, cand), True))

  return len(all_paths)

routes = find_routes(routes)

print('input 1: {0}'.format(routes))
