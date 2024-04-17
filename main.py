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
    
    
def mat_to_list(adj_mat):
    adj_list = []
    for i in range (len(adj_mat)):
        adj_list.append([])
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                adj_list[i].append(j)
                    
    return adj_list
    
    
    
def main():
    adj_mat_test = [[0, 1, 0, 1, 0, 0],
                         [0, 0, 1, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0]]
                         

    
    adj_list_test = mat_to_list(adj_mat_test)
    for i in adj_list_test:
        for j in i:
                print(j , end = " ")
        print()
        
    
    adj_list_test = [[1, 3], [2], [0], [4], [3], []]
    
    reachable_set = reachable(adj_list_test,3)
    print("now for a start node of 3")
    for i in reachable_set:
            print(i , end = " ")
        
    
    

if __name__ == "__main__":
    main()
    
    
