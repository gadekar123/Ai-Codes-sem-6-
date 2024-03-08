from collections import deque

def is_valid(state):
     m1,c1,side= state
     m2= m - m1
     c2 = c-c1 
     if m1 < 0 or m2 < 0 or c1 < 0 or c2 < 0:
        return False
     if (m1 and m1 < c1) or (m2 and m2 < c2):
        return False
     return True

def explore_states(state):
    m1,c1,side = state
    next_states = []
    # lets make possible states based on boat capacity which is always taken as 2
    states = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    for st in states:
        moved_ms ,moved_cn = st

        if side == "left":
            new_state = (m1-moved_ms,c1-moved_cn,"right")
        else:
            new_state = (m1+moved_ms,c1+moved_cn,"left")
        #new state achived but need to check if the state we got is valid or not 
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states


def bfs_mnc(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    all_paths = []
    while queue:
        state_path_pair = queue.popleft()
        state, path = state_path_pair  # Unpack the state and path from the pair
        if state in visited:
            continue
        visited.add(state)
        path.append(state)

        if state == goal_state:
            all_paths.append(path)
            continue
        else:
            for next_state in explore_states(state):
                queue.append((next_state, path.copy()))
    return all_paths



m = int(input("enter total missionaries"))
c = int(input("enter total cannibals"))

if( c!= m ):
    print("please enter equal nunber of missionaries and cannibals")


initial_state = (m,c,"left")
goal_state = (0,0,"right")

paths = bfs_mnc(initial_state,goal_state)

if paths:
        print("Paths found:")
        for path in paths:
            print(path)
else:
        print("No valid paths found.")