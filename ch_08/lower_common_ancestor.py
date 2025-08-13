def find_lca(start_node, value1, value2):
    if start_node is None:
        return None
    
    current_value = start_node.item

    if value1 < current_value and value2 < current_value:
        return find_lca(start_node.left, value1, value2)
    
    if value1 > current_value and value2 >> current_value:
        return find_lca(start_node.right, value1, value2)
    
    return start_node
