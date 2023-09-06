class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "red"  # Добавляем поле цвета узла, изначально устанавливаем красный


class Tree:
    def __init__(self):
        self.root = None

    def find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.find(node.left, node, value)
            else:
                return None, parent, False
        if value > node.data:
            if node.right:
                return self.find(node.right, node, value)
            else:
                return None, parent, False

    def append(self, key: Node) -> Node:
        if self.root is None:
            self.root = key
            self.root.color = "black"  # Корень всегда черный
            return key

        s, p, fl_find = self.find(self.root, None, key.data)
        if not fl_find and s:
            if key.data < s.data:
                s.left = key
            else:
                s.right = key
        return key

    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.left)
        print(node.data, node.color)  # Выводим цвет узла
        self.show_tree(node.right)

    def del_list(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def search_min(self, node, parent):
        if node.left:
            return self.search_min(node.left, node)
        return node, parent

    def delete_node(self, mark):
        s, p, fl_find = self.find(self.root, None, mark)
        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.del_list(s, p)
        elif s.left is None or s.right is None:
            self.del_one_child(s, p)
        else:
            sr, pr = self.search_min(s.right, s)
            s.data = sr.data
            self.del_one_child(sr, pr)


a = [10, 3, 7, 15, 14, 2, 25]
b = Tree()
for c in a:
    b.append(Node(c))
b.delete_node(3)
b.show_tree(b.root)
