import random

# Constants
J = 10
K = 6
L = 3
M = 2
N = 5
Q = 4
# Initialize variables
player_health = 100
gold = 0
arrows = 0
V = 0
X = 0
XW = 0
rooms = [
    {'east': 'A', 'west': 'C'},  # 1
{'east': 'B', 'south': 'D'},  # 2
{'west': 'B', 'south': 'E'},  # 3
{'north': 'A', 'east': 'D'},  # 4
{'west': 'E', 'north': 'C'},  # 5
{'north': 'E', 'west': 'F'},  # 6
{'north': 'F', 'east': 'G'},  # 7
{'east': 'H', 'south': 'G'},  # 8
{'south': 'F', 'east': 'I'},  # 9
{'west': 'H', 'south': 'J'},  # 10
{'north': 'J', 'east': 'I'},  # 11
{'east': 'K', 'west': 'M'},  # 12
{'north': 'L', 'south': 'M'},  # 13
{'north': 'M', 'east': 'N'}  # 14
]

# Trap messages
trap_messages = [
    "STEPPED ON A FROG!",
    "HEAR A SCREAM!",
    "HEAR FOOTSTEPS!",
    "ENCOUNTER A WUMPUS!",
    "HEAR THUNDER!",
    "SNEEZED!",
    "SEE A BAT FLY BY!"
]
