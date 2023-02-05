class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

root = \
    Node(
        Node(
            Node(0, 5),
            Node(8, 4)
        ),
        Node(
            Node(6, 2),
            7
        )
    )

#                root
#               /    \
#              /      \
#             /        \
#            /          \
#           /            \
#          /              \
#         /\              /\
#        /  \            /  \
#       /    \          /    \
#      /      \        /      7
#     /\      /\      /\
#    /  \    /  \    /  \
#   0    5  8    4  6    2

def print_all_nodes(node):
    # Base case
    if not isinstance(node, Node):
        print(node)
        return
    
    # The recursive case
    print_all_nodes(node.left)
    print_all_nodes(node.right)

print_all_nodes(root)