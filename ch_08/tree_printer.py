def subtree_width(height):
    if height <= 0:
        return 0
    
    leaf_width = 3
    spacing = 3

    max_num_of_leaves = pow(2, height - 1)
    width_of_tree = max_num_of_leaves * leaf_width + (max_num_of_leaves - 1) * spacing
    width_of_subtree = (width_of_tree - spacing) // 2

    return width_of_subtree


def stringify_node_value(node):
    if node is None:
        return " "
    if node.item is None:
        return " "
    
    node_value = str(node.item)

    if len(node_value) == 1:
        return " " + node_value + " "
    if len(node_value) == 2:
        return node_value + " "
    
    return node_value[0:3]


def spacing(line_length):
    return " " * line_length


def draw_node(current_node, line_length):
    str_node = " "
    str_node += spacing(line_length)
    str_node += stringify_node_value(current_node)
    str_node += spacing(line_length)

    return str_node


def draw_line(line_length):
    return "-" * line_length


def draw_left_connection_part(node, line_length):
    if node.left is None:
        return " " + spacing(line_length)
    else:
        return draw_line(line_length) + "-| "
    

def draw_right_connection_part(node, line_length):
    if node.right is None:
        return spacing(line_length) + " "
    
    else: 
        return draw_line(line_length) + "-| "


def draw_junction(node):
    if node.left is None and node.right is None:
        return " "
    elif node.left is None:
        return " +-"
    elif node.right is None:
        return "-+ "
    else:
        return "-+-"    


def draw_connections(node, line_length):
    if node is None:
        return " " + spacing(line_length) + " " + spacing(line_length) + " "
    
    connection = draw_left_connection_part(node, line_length)
    connection += draw_junction(node)
    connection += draw_right_connection_part(node, line_length)


