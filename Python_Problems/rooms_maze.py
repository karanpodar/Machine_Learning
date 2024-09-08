from collections import deque

def findShortestPath(start, end, rooms):
    if start == end:
        return [start]
    
    queue = deque([(start, [start])])
    # deque( [(start, [start])])
    visited = set([start])
    
    while queue:
        current_room, path = queue.popleft()
        
        if current_room in rooms:
            for next_room in rooms[current_room]:
                if next_room not in visited:
                    if next_room == end:
                        return path + [next_room]
                    queue.append((next_room, path + [next_room]))
                    visited.add(next_room)
    
    return []

# Example usage:
rooms = {
    'Entrance': ['Hall', 'Kitchen'],
    'Hall': ['Entrance', 'Bedroom', 'Throne'],
    'Kitchen': ['Entrance', 'Cellar'],
    'Bedroom': ['Hall', 'Balcony'],
    'Throne': ['Hall', 'Vault'],
    'Cellar': ['Kitchen', 'Treasure'],
}

start = 'Entrance'
end = 'Treasure'
print(findShortestPath(start, end, rooms))