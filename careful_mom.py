# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def solution(node, elem):
    index = 0
    while True:
        if node == None:
            index = -1
            break
        elif node.value == elem:
            break
        else:
            index += 1
            node = node.next_item
    return index


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "34")
    assert idx == 2

if __name__ == '__main__':
    test()