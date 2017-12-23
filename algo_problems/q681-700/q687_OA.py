# Definition for a binary tree node.
class Node:
    def __init__(self, x, y):
        self.val = x
        self.label = y
        self.children = {}


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    def buildGraphByEdge(self, edge_list, label_list):
        nodes = {}
        for i in range(0, len(edge_list), 2):
            p_key = edge_list[i]
            c_key = edge_list[i + 1]
            if p_key not in nodes:
                nodes[p_key] = Node(p_key, label_list[p_key - 1])
            if c_key not in nodes:
                nodes[c_key] = Node(c_key, label_list[c_key - 1])
            nodes[p_key].children[c_key] = nodes[c_key]
            nodes[c_key].children[p_key] = nodes[p_key]
        return nodes

    def print_nodes(self, nodes):
        for node_key in nodes:
            print(nodes[node_key].val, nodes[node_key].label,
                  nodes[node_key].children.keys())

    def is_cycle(self, nodes):
        visited = {}
        for node_key in nodes:
            if node_key not in visited:
                visited[node_key] = -1
                if self.cycle_find(nodes[node_key], visited, -1, nodes):
                    return True
        return False

    def cycle_find(self, node, visited, parent_key, nodes):
        print(node.val, visited, parent_key)
        for child_key in node.children:
            if child_key in visited:
                if child_key != parent_key and parent_key != -1:
                    print('found cycle', child_key, parent_key)
                    return True
            else:
                visited[child_key] = node.val
                return self.cycle_find(nodes[child_key], visited, node.val, nodes)
        return False


if __name__ == '__main__':
    # nodes = Solution().buildGraphByEdge(
    #     [1, 2, 1, 3, 2, 4, 2, 5], [1, 1, 1, 1, 1])
    # print(nodes)
    # Solution().print_nodes(nodes)
    # print(Solution().is_cycle(nodes))

    nodes = Solution().buildGraphByEdge(
        [1, 2, 1, 3, 2, 4, 2, 5, 4, 5], [1, 1, 1, 1, 1])
    print(nodes)
    Solution().print_nodes(nodes)
    print(Solution().is_cycle(nodes))
