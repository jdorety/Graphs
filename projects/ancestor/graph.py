"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        set_of_friends = self.vertices[v1]
        set_of_friends.add(v2)

    def get_neighbors(self, node):
        return self.vertices[node]

    def bft(self, starting_vertex):
        """
        Class Notes:
        1. Make a queue, so the nodes we are about to visit can wait in line
        2. Make a set, to track all the nodes we have already visited
        3. queue the start node
                While this queue isn't empty:
                a. Dequeue whatever is at the front and this is our current node
                b. if current node has not yet been visited, mark the current node as visited by putting it in our visited set
                c. Get all of the current node's friends / neighbors
                d. For each of those friends:
                        i. Put them into our queue to be visited if not visited yet

        ~~~~~~~~~~~~~~~~~~~~~~
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            current_node = q.dequeue()
            print(current_node)

            if current_node not in visited:
                visited.add(current_node)

                neighbors = self.vertices[current_node]

                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack, for the nodes we are about to visit
        stack = []
        # make a set for visited nodes
        visited = set()
        # put the start node on the stack
        stack.append(starting_vertex)
        # while this stack isn't empty:
        while len(stack):
            # pop off whatever is on top of the stack, this is our current node
            current_node = stack.pop()
            print(current_node)
            # if current node has not yet been visited:
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.vertices[current_node]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

            # mark the current node as visited by putting it in our visited set
            # get all of the current node's friends / neighbors
            # for each of those friends:
            #   put them into our stack to be visited

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # base case: node has been visited, didn't do anything, just return
        node = starting_vertex
        if node not in visited:
            print(node)
            visited.add(node)
            neighbors = self.vertices[node]
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        path = [starting_vertex]
        q.enqueue(path)

        while q.size() > 0:
            current_path = q.dequeue()

            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    path_copy = current_path[:]

                    path_copy.append(neighbor)

                    q.enqueue(path_copy)

        return path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("vanilla DFT")
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("vanilla BFT")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("recursive DFT")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
