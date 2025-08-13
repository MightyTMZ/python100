class Queue:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def enqueue(self, val):
        self.values.append(val)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"    
        return self.values[0]

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.values.pop(0)


def level_sum(start_node):
    if start_node is None:
        return {}
    
    result = {}

    to_process = Queue()

    to_process.enqueue((start_node, 0))

    while not to_process.is_empty():
        current_node_and_level = to_process.dequeue()
        
        current_node = current_node_and_level[0]
        level = current_node_and_level[1]

    if level not in result:
        result[level] = 0

    result[level] += current_node.item

    if current_node.left is not None:
        to_process.enqueue((current_node.left, level + 1))

    if current_node.right is not None:
        to_process.enqueue((current_node.right, level + 1))

    return result


# Helper method
def traverse_depth_first(current_node, level, results):
    if current_node:
        # PREORDER
        traverse_depth_first(current_node.left, level + 1, results)


    # INORDER    
    results[level] = results.get(level, 0) + current_node.item
    traverse_depth_first(current_node.right, level + 1, results)

    # POSTORDER
    results[level] = results.get(level, 0) + current_node.item


def level_sum_depth_first(root):
    results = {}

    traverse_depth_first(root, 0, results)

    return dict(sorted(results.items()))



from example_trees import create_example_level_sum_tree

def main():
    root = create_example_level_sum_tree()

    result = level_sum(root)
    print("\nLevel sum:", result)


if __name__ == "__main__":
    main()