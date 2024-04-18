from collections import deque

def JugBFS(start, goal, jL, jR):
    queue = deque([(start, [(0, 0)])])
    visited = set()

    while queue:
        curr_state, path = queue.popleft()
        L, R = curr_state

        if L == goal or R == goal:
            all_paths.append(path)
            continue

        visited.add(curr_state)

        states = [(jL, R), (L, jR), (0, R), (L, 0)]

        # pour from right jug to left jug
        pour_left = jL - L
        if pour_left >= R:
            states.append((L + R, 0))
        else:
            states.append((jL, R - pour_left))

        # pour from left jug to right jug
        pour_right = jR - R
        if pour_right >= L:
            states.append((0, L + R))
        else:
            states.append((L - pour_right, jR))

        for s in states:
            if s not in visited:
                queue.append((s, path + [s]))
                visited.add(s)


all_paths = []

goal = int(input('Enter goal: '))
jugL = int(input('Enter capacity of left jug: '))
jugR = int(input('Enter capacity of right jug: '))
JugBFS((0, 0), goal, jugL, jugR)

if len(all_paths) == 0:
    print('No possible solutions')
else:
    for path in all_paths:
        print(path)
