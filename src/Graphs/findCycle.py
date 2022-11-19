# Example graphs
#   0 --> 1 --> 2
#
#    4 --> 44
#    ^
#   /
#  3----> 6
#   ^    /
#    \  v
#     8

class Graph:
    def __init__(self,graph_src_to_dst_list=None):
        if graph_src_to_dst_list == None:
            self.src_to_dst_list = None
        else:
            self.src_to_dst_list = graph_src_to_dst_list
            
def has_cycles(graph):
    
    for node in graph.src_to_dst_list:
        
        visited = {node}
        
        if dfs(graph, node, visited):
            return True
        
    return False

def dfs(graph, node, visited):
    
    connections = graph.src_to_dst_list[node]
    
    if len(connections) == 0:
        return False
    
    for edge in connections:
        
        if edge in visited:
            return True
        
        _visited = visited.copy()
        _visited.add(edge)

        if dfs(graph, edge, _visited):
            return True
        
        _visited.remove(edge)       

def verify(expected, result):
    if expected == result:
        print("Pass")
        
    else:
        print("Fail")

graph1 = Graph({
    0 : [ 1 ],
    1 : [ 0 ]
})

verify( True,has_cycles(graph1))

graph2 = Graph({
    0 : [ 1 ],
    1 : [ 2 ],
    2 : [ ]
})
verify(False,has_cycles(graph2))


graph3 = Graph({
    0 : [ 1 ],
    1 : [ 2 ],
    2 : [ ],
    3 : [ 4, 6],
    4 : [ 44 ],
    44: [],
    6: [8],
    8: [3]
    
})
verify(True,has_cycles(graph3))

graph4 = Graph({
})
verify(False,has_cycles(graph4))

graph5 = Graph({
    2 : [ ],
    1 : [ 2 ],
    0 : [ 1 ],
})
verify(False,has_cycles(graph5))

graph6 = Graph({
    0 : [ 1 ],
    1 : [ 2 ],
    2 : [ ],
    3 : [ 4, 6],
    4 : [ 44 ],
    44: [],
    6: [8, 4],
    8: []
    
})
verify(False,has_cycles(graph6))
