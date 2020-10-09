from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = {}
reverse_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}
reverse = []
rooms_left = []

# loop through while room_graph is larger than visited set
while len(room_graph) > len(visited):

    # assign player's current room to variable
    current = player.current_room.id

    # assign current room's exits to variable
    exits = player.current_room.get_exits()

    # append current into rooms_left array
    rooms_left.append(current)

    # assign current room's exits if not in visited
    if current not in visited:
        visited[current] = exits

    # runs if the length of visited at current index is less than 0
    if len(visited[current]) > 0:

        # pop current in visited array
        v = visited[current].pop()

        # append visited room to traversal_path array
        traversal_path.append(v)

        # append to reverse direction array
        reverse.append(reverse_direction[v])

        # send player to visited room
        player.travel(v)

    else:
        # send player in the reverse direction if no exit
        r = reverse.pop()
        traversal_path.append(r)
        player.travel(r)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
