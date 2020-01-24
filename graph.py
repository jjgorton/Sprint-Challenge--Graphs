class Graph:
    def __init__(self):
        self.rooms = {}
    
    def add_room(self, room_id, exits):
        self.rooms[room_id] = {}
        for direction in exits:
            self.rooms[room_id][direction] = '?'


    def add_connection(self, prev_room, cur_room, direction):
        opp_dir = ''
        if direction == 'n':
            opp_dir = 's'
        elif direction == 's':
            opp_dir = 'n'
        elif direction == 'w':
            opp_dir == 'e'
        elif direction == 'e':
            opp_dir = 'w'

        self.rooms[prev_room][direction] = cur_room
        self.rooms[cur_room][opp_dir] = prev_room


    def bfs_paths(self, room_id):
        
        q = Queue()
        #change user_id to a direction that is unexplored
        exits = []
        for direction in self.rooms[room_id]:
            if direction == '?':
                exits.append(direction)
        direction = exits[0]
        q.enqueue([direction])
        visited = {}

        while q.size() > 0:
            path = q.dequeue()
            room = path[-1]

            if user not in visited:
                visited[user] = path

                for friend in self.friendships[user]:
                    new_path = list(path)
                    new_path.append(friend)
                    if friend not in visited:
                        q.enqueue(new_path)

        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
        #    Pop the first item
            vertex = stack.pop()
        #    If not visited
            if vertex not in visited:
        #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
        #           Add that edge to the queue/stack
                    stack.push(next_vert)

    def bfs(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enstack a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #    Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
        #    If not visited
            if vertex not in visited:
                if vertex == '?':
                    # Do the thing!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                # Copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    queue.enqueue(new_path)