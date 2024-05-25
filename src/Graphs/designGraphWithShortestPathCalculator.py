# Leetcode 2642 - Hard
# There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

# Implement the Graph class:

# Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
# addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
# int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
 

# Example 1:
# Input
# ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
# [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
# Output
# [null, 6, -1, null, 6]

# Explanation
# Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
# g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
# g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
# g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
# g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.
 

# Constraints:
# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1)
# edges[i].length == edge.length == 3
# 0 <= fromi, toi, from, to, node1, node2 <= n - 1
# 1 <= edgeCosti, edgeCost <= 106
# There are no repeated edges and no self-loops in the graph at any point.
# At most 100 calls will be made for addEdge.
# At most 100 calls will be made for shortestPath.

from typing import List
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = {}
        self.nodes = set()
        for edge in edges:
            self.addEdge(edge)
        
        

    def addEdge(self, edge: List[int]) -> None:
        self.n += 1
        self.nodes.add(edge[0])
        self.nodes.add(edge[1])
        if edge[0] in self.edges:
            self.edges[edge[0]].append(edge)
        else:
            self.edges[edge[0]] = [edge]
        
    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        if node1 not in self.nodes or node2 not in self.nodes:
            return -1

        #initialize lowestCost table. Distance to start node is 0
        lowestCost = {i: float("inf") for i in self.nodes}
        lowestCost[node1] = 0
        #initialize processed nodes set to prevent loops
        processedNodes = set()
        processedNodes.add(node1)

        def updateCosts(edges):
            for edge in edges:
                srcNode, dstNode, cost  = edge
                lowestCost[dstNode] = min(lowestCost[srcNode]+cost, lowestCost[dstNode])
            

        def getNextNode():
            nodeVal = float("inf")
            node = self.n
            
            
            for i in self.nodes - processedNodes:
                if lowestCost[i] < nodeVal:
                    nodeVal = lowestCost[i]
                    node = i
            return node
        
        if node1 in self.edges:
            updateCosts(self.edges[node1])


        while len(processedNodes) < len(self.nodes):
            node = getNextNode()
            if node == self.n:
                break
            
            if node in self.edges:
                updateCosts(self.edges[node])
            
            processedNodes.add(node)
        
        return lowestCost[node2] if lowestCost[node2] != float("inf") else -1

class GraphMaker:

    def __init__(self, sequence, inputData, expected):
        
        self.graph = Graph(inputData[0][0], inputData[0][1])
        self.output = [None]
        self.answer = expected
        
        for step, data in zip(sequence[1:], inputData[1:]):
            
            if step == 'addEdge':
                self.graph.addEdge(data[0])
                self.output.append(None)
            elif step == 'shortestPath':
                self.output.append(self.graph.shortestPath(data[0], data[1]))

    def verifyResult(self):
        return self.output == self.answer
            



if __name__ == '__main__':

    sequence = ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
    inputData = [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
    answer = [None, 6, -1, None, 6]

    builder = GraphMaker(sequence, inputData, answer)
    print(builder.verifyResult())


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)