def reachable(adj_list, start_node):
    length = len(adj_list)
    visited = []
    stack = [start_node]
    for i in range(length):
        visited.append(False)
    while stack:
        current_node = stack.pop()
        if visited[current_node] == False:
            visited[current_node] = True
            for neighbor in adj_list[current_node]:
                stack.append(neighbor)
    
    reachable = set()
    for j in range(length):
        if visited[j] ==  True:
            reachable.add(j)
    
    return reachable