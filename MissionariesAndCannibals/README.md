# 传教士野人过河问题

## 问题说明

传教士野人过河问题是经典的人工智能问题，涉及到状态空间搜索。目的是将三个传教士和三个野人安全地从河的一岸渡到另一岸，遵循以下规则：

1. 每次渡船最多可载两个人。
2. 在任何时刻，野人的数量不能超过传教士的数量，否则传教士会面临危险。

## 状态空间表示

在状态表示中，使用一个元组 `(m, c, b)` 来表示当前的状态，其中：

- `m` 是岸上的传教士数量。
- `c` 是岸上的野人数。
- `b` 表示船的位置，`1` 表示在起始岸，`0` 表示在对岸。

```python
class Node:
    def __init__(self, state, parent):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node


# Initial state: 3 missionaries, 3 cannibals, boat on starting side
initialState = (3, 3, 1)
# Goal state: 0 missionaries, 0 cannibals, boat on other side
goalState = (0, 0, 0)
```

##  状态转移图

状态转移通过定义可能的动作来实现，这些动作包括：

- `(0, 1)`：一个野人过河。
- `(1, 0)`：一个传教士过河。
- `(2, 0)`：两个传教士过河。
- `(0, 2)`：两个野人过河。
- `(1, 1)`：一个传教士和一个野人过河。

在每个状态下，生成下一个可能的状态，并通过 `isValid` 函数确保新状态是有效的。

```python
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
```

## 遍历状态图

使用深度优先搜索（DFS）算法遍历状态图，找到所有从初始状态到目标状态的路径。当找到目标状态时，记录路径。该方法保证了所有可能的解决方案都被找到。

```python
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
```

## 输出结果

最终，代码会输出所有可能的过河方案。这些方案在状态转移图中呈现为路径，确保在每一步都满足传教士和野人的数量条件。这样就可以充分探索所有解决方案，确保问题的最终目标得以实现。

```python
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
```

结果如下所示，分别展示 DFS 和 BFS 两种算法，共搜索到4种解决方案。

![image-20240925113929894](.\resultDFS.png)

![image-20240925113929894](.\resultBFS.png)