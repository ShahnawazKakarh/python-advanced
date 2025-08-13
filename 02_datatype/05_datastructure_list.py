# Lists in Python
# Lists are mutable sequences, typically used to store collections of homogeneous items.
# They can contain elements of different data types, including other lists.
# Lists are created using square brackets [].

my_list = [1, 2, 3, 4, 5]  # Example of a list

# Lists can be used to store complex data structures, such as dictionaries or other lists.
complex_structure = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    [1, 2, 3]
]  # Example of a complex data structure
print(complex_structure)  # Output: [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, [1, 2, 3]]

# You can access elements in a complex structure using multiple indices and keys.
alice_age = complex_structure[0]["age"]  # Accessing Alice's age
print(alice_age)  # Output: 30

# You can also iterate over a complex structure using loops.
for item in complex_structure:
    if isinstance(item, dict):
        print(f"Name: {item['name']}, Age: {item['age']}")
    elif isinstance(item, list):
        print(f"List: {item}")
# Output:
# Name: Alice, Age: 30
# Name: Bob, Age: 25
# List: [1, 2, 3]
# Lists can be used to store data in a structured way, making them useful for various applications.
# For example, you can use lists to store user inputs, results of computations, or any other data that needs to be organized.
# Lists can also be used to implement algorithms, such as searching and sorting.
# For example, you can implement a simple linear search algorithm using a list.
def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:

            return index  # Return the index of the target element
    return -1

# Example usage of linear search
search_list = [10, 20, 30, 40, 50]
target_value = 30
index = linear_search(search_list, target_value)

if index != -1:
    print(f"Element {target_value} found at index {index}.")
else:
    print(f"Element {target_value} not found in the list.")

# Output: Element 30 found at index 2.
# Lists can also be used to implement sorting algorithms, such as bubble sort.
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Example usage of bubble sort
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)

print("Sorted list:", sorted_list)  # Output: Sorted list: [11, 12, 22, 25, 34, 64, 90]

# Lists can also be used to implement more complex data structures, such as stacks and queues.
# For example, you can implement a stack using a list.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
# Example usage of Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack size:", stack.size())  # Output: Stack size: 3
print("Top element:", stack.peek())  # Output: Top element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2

# Lists can also be used to implement a queue.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        
        return None
    
# Example usage of Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue size:", queue.size())  # Output: Queue size: 3
print("Front element:", queue.peek())  # Output: Front element: 1
print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 1
print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2

# Lists can also be used to implement more complex data structures, such as linked lists, trees, and graphs.
# For example, you can implement a simple linked list using a class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")

# Example usage of LinkedList
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()  # Output: 1 -> 2 -> 3 -> None

# Lists can also be used to implement more complex data structures, such as trees and graphs.
# For example, you can implement a simple binary tree using a class.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(node.right, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

# Example usage of BinaryTree
binary_tree = BinaryTree()
binary_tree.insert(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(8)
print("Inorder traversal of the binary tree:")
binary_tree.inorder_traversal(binary_tree.root)  # Output: 2 3 4 5 6 7 8

# Lists can also be used to implement graphs using adjacency lists.
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(map(str, self.graph[vertex]))}")

# Example usage of Graph
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
print("Graph adjacency list:")
graph.display()  # Output: 1: 2, 3; 2: 1, 4; 3: 1, 4; 4: 2, 3


# Lists can also be used to implement algorithms, such as searching and sorting.
# For example, you can implement a simple binary search algorithm using a sorted list.
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid  # Return the index of the target element
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage of binary search
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
index = binary_search(sorted_list, target_value)
if index != -1:
    print(f"Element {target_value} found at index {index}.")
else:
    print(f"Element {target_value} not found in the list.")
# Output: Element 5 found at index 4.

# Lists can also be used to implement sorting algorithms, such as quicksort.
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)
# Example usage of quicksort
unsorted_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(unsorted_list)
print("Sorted list using quicksort:", sorted_list)  # Output: Sorted list using quicksort: [1, 1, 2, 3, 6, 8, 10]


# Lists can also be used to implement more complex algorithms, such as Dijkstra's algorithm for finding the shortest path in a graph.
import heapq
def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Example usage of Dijkstra's algorithm
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)
print("Shortest paths from vertex A:", shortest_paths)  # Output: Shortest paths from vertex A: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

# Lists can also be used to implement more complex data structures, such as heaps and priority queues.
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def peek(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
# Example usage of MinHeap
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(8)
print("Min element:", min_heap.peek())  # Output: Min element: 3
print("Extracted min:", min_heap.extract_min())  # Output: Extracted min: 3
print("Min element after extraction:", min_heap.peek())  # Output: Min element after extraction: 5

# Lists can also be used to implement more complex algorithms, such as dynamic programming.
def fibonacci(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# Example usage of Fibonacci function
n = 10
fib_number = fibonacci(n)
print(f"Fibonacci number at position {n} is {fib_number}.")  # Output: Fibonacci number at position 10 is 55

# Lists can also be used to implement more complex algorithms, such as backtracking.
def backtrack(choices, current_choice, results):
    if len(current_choice) == len(choices):
        results.append(current_choice.copy())
        return
    for choice in choices:
        if choice not in current_choice:
            current_choice.append(choice)
            backtrack(choices, current_choice, results)
            current_choice.pop()

# Example usage of backtracking
choices = [1, 2, 3]
results = []
backtrack(choices, [], results)
print("All combinations:", results)  # Output: All combinations: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] 


# Lists can also be used to implement more complex algorithms, such as graph traversal algorithms like breadth-first search (BFS) and depth-first search (DFS).
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage of BFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("BFS traversal starting from vertex A:")
bfs(graph, 'A')  # Output: BFS traversal starting from vertex A: A B C D E F

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage of DFS
print("\nDFS traversal starting from vertex A:")
dfs(graph, 'A')  # Output: DFS traversal starting from vertex A: A B D E F C


# Lists can also be used to implement more complex algorithms, such as sorting algorithms like merge sort.
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Example usage of merge sort
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print("Sorted list using merge sort:", sorted_list)  # Output: Sorted list using merge sort: [3, 9, 10, 27, 38, 43, 82]


# Lists can also be used to implement more complex algorithms, such as quicksort.
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage of quicksort
unsorted_list = [10, 7, 8, 9, 1, 5]
sorted_list = quicksort(unsorted_list)
print("Sorted list using quicksort:", sorted_list)  # Output: Sorted list using quicksort: [1, 5, 7, 8, 9, 10]


# Lists can also be used to implement more complex algorithms, such as dynamic programming algorithms.
def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# Example usage of knapsack problem
weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6
max_value = knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)  # Output: Maximum value in knapsack: 55

# Lists can also be used to implement more complex algorithms, such as the A* search algorithm for pathfinding.
import heapq
def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {vertex: float('infinity') for vertex in graph}
    g_score[start] = 0
    f_score = {vertex: float('infinity') for vertex in graph}
    f_score[start] = heuristic(start, goal)
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return []


def heuristic(a, b):
    # Example heuristic function (Euclidean distance)
    return abs(ord(a) - ord(b))


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]  # Return reversed path


# Example usage of A* search algorithm
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}
start_vertex = 'A'
goal_vertex = 'F'
path = a_star(graph, start_vertex, goal_vertex)
print("Path from A to F:", path)  # Output: Path from A to F: ['A', 'B', 'D', 'E', 'F']


# Lists can also be used to implement more complex algorithms, such as the Floyd-Warshall algorithm for finding shortest paths in a weighted graph.
def floyd_warshall(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u in vertices:
        for v, weight in graph[u].items():
            dist[vertices.index(u)][vertices.index(v)] = weight
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Example usage of Floyd-Warshall algorithm
graph = {
    'A': {'B': 3, 'C': 8},
    'B': {'A': 3, 'C': 2, 'D': 5},
    'C': {'A': 8, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
shortest_paths = floyd_warshall(graph)
print("Shortest paths matrix:")
for row in shortest_paths:
    print(row)  # Output: Shortest paths matrix: [0, 3, 5, 6], [3, 0, 2, 3], [5, 2, 0, 1], [6, 3, 1, 0]

# Lists can also be used to implement more complex algorithms, such as the Bellman-Ford algorithm for finding shortest paths in a graph with negative weights.
def bellman_ford(graph, start):
    vertices = list(graph.keys())
    n = len(vertices)
    dist = {vertex: float('inf') for vertex in vertices}
    dist[start] = 0
    for _ in range(n - 1):
        for u in vertices:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    return dist

# Example usage of Bellman-Ford algorithm
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': -3},
    'D': {'B': 5, 'C': -3}
}
start_vertex = 'A'
shortest_paths = bellman_ford(graph, start_vertex)
print("Shortest paths from A:", shortest_paths)  # Output: Shortest paths from A: {'A': 0, 'B': 1, 'C': 3, 'D': -2}


# Lists can also be used to implement more complex algorithms, such as the KMP algorithm for substring search.
def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m  # Longest Prefix Suffix array
    j = 0  # Length of previous longest prefix suffix
    compute_lps(pattern, m, lps)
    i = 0  # Index for text
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def compute_lps(pattern, m, lps):
    length = 0  # Length of previous longest prefix suffix
    lps[0] = 0  # lps[0] is always 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

# Example usage of KMP search
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)  # Output: Pattern found at index 10


# Lists can also be used to implement more complex algorithms, such as the Rabin-Karp algorithm for substring search.
def rabin_karp_search(text, pattern):
    d = 256  # Number of characters in the input alphabet
    q = 101  # A prime number
    m = len(pattern)
    n = len(text)
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1

    for i in range(m - 1):
        h = (h * d) % q


    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                print(f"Pattern found at index {i}")
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

# Example usage of Rabin-Karp search
text = "GEEKS FOR GEEKS"
pattern = "GEEK"
rabin_karp_search(text, pattern)  # Output: Pattern found at index 0, Pattern found at index 10


# Lists are versatile data structures in Python that can hold an ordered collection of items.
# They can be used to store various data types, including numbers, strings, and even other lists.
# Lists can be modified by adding, removing, or changing elements, making them suitable for dynamic data storage.
# They support various operations such as indexing, slicing, and iteration, allowing for efficient data manipulation.
# Lists can also be used to implement complex algorithms and data structures, such as stacks, queues, and graphs.
# Overall, lists are a fundamental part of Python programming and are widely used in various applications.



# --- IGNORE ---