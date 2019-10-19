from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    family_tree = Graph()
    
    for ancestor in ancestors:
        if ancestor[0] not in family_tree.vertices.keys():
            family_tree.add_vertex(ancestor[0])
        family_tree.add_edge(ancestor[0], ancestor[1])
    
    