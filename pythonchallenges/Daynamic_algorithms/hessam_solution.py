import random


class Tree:

    def __init__(self, depth=5):
        self.depth = depth
        self.tree = self.generate_tree_sample()

    def generate_tree_sample(self):
        tree = list()
        [tree.append(random.sample(range(1, 1000), i)) for i in range(1, self.depth + 2)]
        return tree


class MaxPath:

    def __init__(self, tree):
        self.tree = tree

    def calculate_path(self):
        
        max_list = list()
        print(self.tree)
        self.tree.reverse()
        
        for row in self.tree:
            print('before sum', row)
            if max_list:
                row = [sum(s) for s in zip(row, max_list)]
            print('after sum', row)
                
            max_list = list()
            for i in range(len(row)-1):
                max_list.append(max(row[i], row[i+1]))


if __name__ == '__main__':
    tree_obj = Tree(depth=3)
    tree = tree_obj.generate_tree_sample()
    print(tree)
    
    maxpath_obj = MaxPath(tree)
    maxpath_obj.calculate_path()
