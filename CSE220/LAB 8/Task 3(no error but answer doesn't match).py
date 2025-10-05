def loads(tasks, m):
    machine_heap = MinHeap(m)
    size=len(tasks)
    for i in range(m):
        machine_heap.insert(0)

    for task in tasks:
      if size>m:
        min_load = machine_heap.extractMin()
        updated_load = min_load + task
        machine_heap.insert(updated_load)

    return machine_heap.getheap()

#DRIVER CODE
tasks = [2, 4, 7, 1, 6]
m = 4
print(loads(tasks,m))