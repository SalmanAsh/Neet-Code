def minimumSwaps(popularity):
    n = len(popularity)
    positions = []
    
    for i in range(n):
        positions.append((popularity[i], i))
        
    positions.sort()
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        # If element is already visited or already in the correct position
        if visited[i] or positions[i][1] == i:
            continue
        
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = positions[j][1]
            cycle_size += 1
        
        swaps += (cycle_size - 1)
    
    return swaps