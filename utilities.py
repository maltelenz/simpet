from math import sqrt

# Utilities
def shift_position_up(pos):
    return (pos[0], pos[1] + 1)

def shift_position_down(pos):
    return (pos[0], pos[1] - 1)

def shift_position_left(pos):
    return (pos[0] - 1, pos[1])

def shift_position_right(pos):
    return (pos[0] + 1, pos[1])

def are_neighbors(p1, p2):
    # Everything on the neighboring 8 squares is a neighbor
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) < 1.5