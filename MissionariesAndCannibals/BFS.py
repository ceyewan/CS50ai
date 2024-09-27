from collections import deque


# Initial state: 3 missionaries, 3 cannibals, boat on starting side
initialState = (3, 3, 1)
# Goal state: 0 missionaries, 0 cannibals, boat on other side
goalState = (0, 0, 0)


def isValid(state):
    m, c, _ = state  # Unpack state into m (missionaries) and c (cannibals)
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    if (m > 0 and m < c) or (m < 3 and m > c):
        return False
    return True



# Generate possible successor states based on moves
def successors(state):
    moves = [(0, 1), (1, 0), (2, 0), (0, 2), (1, 1)]
    for move in moves:
        if state[2] == 1:
            newState = (state[0] - move[0], state[1] - move[1], 0)
        else:
            newState = (state[0] + move[0], state[1] + move[1], 1)
        if isValid(newState):
            yield newState


# Perform BFS to find all paths to the goal node
def findPathsBFS(state, goalState):
    paths = []
    queue = deque([(state, [state])])
    while queue:
        (state, path) = queue.popleft()
        for nextState in successors(state):
            if nextState not in path:
                if nextState == goalState:
                    paths.append(path + [nextState])
                queue.append((nextState, path + [nextState]))
    return paths


def showResult():
    paths = findPathsBFS(initialState, goalState)
    if paths is None:
        print("没有找到解法.")
        return
    for index, path in enumerate(paths):
        print(f"解法 {index + 1}:")
        for i in range(1, len(path)):
            state = path[i]
            previousState = path[i - 1]
            missionariesMoved = abs(state[0] - previousState[0])
            cannibalsMoved = abs(state[1] - previousState[1])
            movement = "渡河" if state[2] == 0 else "返回"
            description = f"{missionariesMoved}传教士和{cannibalsMoved}野人{movement}"
            print(f"\t状态: {previousState} -> 状态: {state} by {description}.")

showResult()
