def JugIterative(start,goal,jL,jR):
    stack = [(start, [(0, 0)])]
    visited = set()

    while stack:
        curr_state, path = stack.pop()
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
                stack.append((s, path + [s]))


all_paths = []

goal =int(input('enter goal'))
jugL = int(input('enter capacity of left jug'))
jugR = int(input('enter capacity of right jug'))
JugIterative((0, 0),goal,jugL,jugR)

if len(all_paths) == 0 :
    print('No possible solutions')
else :
    for path in all_paths:
        print(path)