class Node:
    def __init__(self, state, parent):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node


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


# Generate possible successor states based on movesF
def successors(state):
    moves = [(0, 1), (1, 0), (2, 0), (0, 2), (1, 1)]
    for move in moves:
        if state[2] == 1:
            newState = (state[0] - move[0], state[1] - move[1], 0)
        else:
            newState = (state[0] + move[0], state[1] + move[1], 1)
        if isValid(newState):
            yield newState


explored = set()
paths = []


# Perform DFS to find all paths to the goal node
def findPathsDFS(node, goalState):
    if node.state == goalState:
        path = []
        while node is not None:
            path.append(node.state)
            node = node.parent
        paths.append(path[::-1])
        return
    explored.add(node.state)
    for state in successors(node.state):
        newNode = Node(state, node)
        if state not in explored:
            findPathsDFS(newNode, goalState)
    explored.remove(node.state)

def showResult():
    findPathsDFS(Node(initialState, None), goalState)
    if paths is None:
        print("No solution found.")
        return
    for index, path in enumerate(paths):
        print(f"Solution {index + 1}:")
        for i in range(1, len(path)):
            state = path[i]
            previousState = path[i - 1]
            missionariesMoved = abs(state[0] - previousState[0])
            cannibalsMoved = abs(state[1] - previousState[1])
            movement = "crosses" if state[2] == 0 else "returns"
            description = f"{missionariesMoved} missionaries and {cannibalsMoved} cannibals {movement}"
            print(f"\tState: {previousState} -> State: {state} with {description}.")

showResult()
