# Consider using a tree to model mathematical expressions with the four operators +, -, /, and *

def evaluate(node):
    value = node.item

    match value:
        case "+" | "-" | "*" | "/":
            val1 = evaluate(node.left)
            val2 = evaluate(node.right)
            return eval(str(val1) + value + str(val2))
        case _: 
            return int(value)