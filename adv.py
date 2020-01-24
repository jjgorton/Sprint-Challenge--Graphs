from room import Room
from player import Player
from world import World
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = Graph()
unexplored = []
visited = set()

# initialize with first room:
room = player.current_room
prev_room = room
exits = room.get_exits()
graph.add_room(room.id, exits)
visited.add(room)
for way in graph.rooms[player.current_room.id]:
    if graph.rooms[room.id][way] == '?':
        unexplored.append(way)

direction = exits[random.randint(0, len(exits)-1)]

while len(unexplored) > 0:
    # Move to new room
    player.travel(direction)
    traversal_path.append(direction)

    room = player.current_room
    exits = room.get_exits()

    if room not in visited:
        graph.add_room(room.id, exits)
        visited.add(room)

    if prev_room is not None: # checks for first time only
        graph.add_connection(prev_room.id, room.id, direction)
    prev_room = room

    # reset for next loop
    unexplored = []
    for way in graph.rooms[player.current_room.id]:
        if graph.rooms[player.current_room.id][way] == '?':
            unexplored.append(way)
    if len(unexplored) > 0:
        direction = unexplored[0]
    else:
        #BFS for '?'
        to_new_route = graph.bfs(player.current_room.id)
        print(f'dead end {traversal_path}')
        if to_new_route is not None:
            for direction in to_new_route:
                player.travel(direction)
                traversal_path.append(direction)
            prev_room = player.current_room
            for way in graph.rooms[player.current_room.id]:
                if graph.rooms[player.current_room.id][way] == '?':
                    unexplored.append(way)
            if len(unexplored) > 0:
                direction = unexplored[0]
            
    
    print(graph.rooms)
    
print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
