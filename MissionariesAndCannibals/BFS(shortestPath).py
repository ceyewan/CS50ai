class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []
    def add(self, node):
        self.frontier.append(node)
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
initialNode = Node((3, 3, 1), None, None)
goalNode = Node((0, 0, 0), None, None)


def isValid(state):
    m, c, _ = state  # Unpack state into m (missionaries) and c (cannibals)
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    if (m > 0 and m < c) or (m < 3 and m > c):
        return False
    return True


def successors(state):
    moves = [(0, 1), (1, 0), (2, 0), (0, 2),(1, 1)]
    for move in moves:
        if state[2] == 1:
            newState = (state[0] - move[0], state[1] - move[1], 0)
        else:
            newState = (state[0] + move[0], state[1] + move[1], 1)
        if isValid(newState):
            yield state[2], newState


def findPath(initialNode, goalNode):
    frontier = StackFrontier() # StackFrontier()
    frontier.add(initialNode)
    explored = set()
    while not frontier.empty():
        node = frontier.remove()
        if node.state == goalNode.state:
            path = []
            while node is not None:
                path.append((node.action, node.state))
                node = node.parent
            return path[::-1]
        explored.add(node.state)
        for action, state in successors(node.state):
            if not frontier.contains_state(state) and state not in explored:
                frontier.add(Node(state, node, action))
    return None
    
def showResult():
    path = findPath(initialNode, goalNode)
    if path is None:
        print("No solution found")
        return
    for i in range(1, len(path)):
        action, state = path[i]
        previousState = path[i-1][1]
        missionariesMoved = abs(state[0] - previousState[0])
        cannibalsMoved = abs(state[1] - previousState[1])
        movement = "returns" if action == 0 else "crosses"
        description = f"{missionariesMoved} missionaries and {cannibalsMoved} cannibals {movement}"
        print(f"\tState: {previousState} -> State: {state} with {description}.")
        
showResult()