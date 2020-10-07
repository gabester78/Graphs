from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node):
    # transfer ancestors (key: value) to dict type
    dict = {}
    for x, y in ancestors:
        if x not in dict:
            dict[x] = [y]
        else:
            dict[x].append(y)

    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    v = starting_node
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            for next_node in get_neighbors(dict, v):
                new_arr = path.copy()
                new_arr.append(next_node)
                q.enqueue(new_arr)

    if v == starting_node:
        return -1
    return v


def get_neighbors(dict, node):
    neighbors = []
    two_parents = 0
    for x, y in dict.items():
        if node in y:
            neighbors.append(x)
    for n in neighbors:
        if len(get_neighbors(dict, n)) == 0:
            two_parents += 1
        if two_parents == 2:
            neighbors = [min(neighbors)]
    return neighbors
