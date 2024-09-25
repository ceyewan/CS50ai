class Node:
    def __init__(self, state, parent, action):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node
        self.action = action  # Action taken to reach this node


# Initial state: 3 missionaries, 3 cannibals, boat on starting side
initialNode = Node((3, 3, 1), None, None)
# Goal state: 0 missionaries, 0 cannibals, boat on other side
goalNode = Node((0, 0, 0), None, None)


def isValid(state):
    if state[0] < 0 or state[1] < 0 or state[2] < 0:
        return False
    if state[0] > 3 or state[1] > 3 or state[2] > 1:
        return False
    if state[0] > 0 and state[0] < state[1]:
        return False
    if state[0] < 3 and state[0] > state[1]:
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
            yield state[2], newState


explored = set()
paths = []


# Perform DFS to find all paths to the goal node
def findPathsDFS(node, goalNode):
    if node.state == goalNode.state:
        path = []
        while node is not None:
            path.append((node.action, node.state))
            node = node.parent
        paths.append(path)
        return
    explored.add(node.state)
    for action, state in successors(node.state):
        newNode = Node(state, node, action)
        if state not in explored:
            findPathsDFS(newNode, goalNode)
    explored.remove(node.state)

def showResult():
    findPathsDFS(initialNode, goalNode)
    if paths is None:
        print("No solution found.")
        return
    for index, path in enumerate(paths):
        print(f"Solution {index + 1}:")
        for i in range(1, len(path)):
            action, state = path[i]
            previousState = path[i - 1][1]
            missionariesMoved = abs(state[0] - previousState[0])
            cannibalsMoved = abs(state[1] - previousState[1])
            movement = "returns" if action == 0 else "crosses"
            description = f"{missionariesMoved} missionaries and {cannibalsMoved} cannibals {movement}"
            print(f"\tState: {previousState} -> State: {state} with {description}.")

showResult()
