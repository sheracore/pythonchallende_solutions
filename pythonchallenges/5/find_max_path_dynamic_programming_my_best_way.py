from platform import node
import random


class MakeTree():

    def __init__(self, depth=5):
        self.depth = depth
        self.tree, self.values = self.generate_tree_sample()

    def generate_tree_sample(self):
        self.nodes_count = 2**self.depth-1
        values_count = 2**(self.depth+1)
        print(self.nodes_count)
        values = [random.randint(1,1000) for _ in range(1,values_count)]
        nodes_index_binary_tree = dict()
        
        for i in range(1, self.nodes_count+1):
            nodes_index_binary_tree[i] = [2*i, 2*i+1]
            nodes_index_binary_tree[2*i] = [i]
            nodes_index_binary_tree[2*i+1] = [i]
            
        
        return nodes_index_binary_tree, values

class MaxPath():
    dp = [0]*20
    
    # def __init__(self, depth):
    #     super().__init__(depth)
    #     print(self.depth, self.values, self.dp)

    def find_sum_pathes(self, values, tree, child, parent):
        print(values, tree, child)
        MaxPath.dp[child] = values[child-1]    
        maximum = 0
        
        for child_index in tree[child]:
            if child_index == parent:
                continue
            
            self.find_sum_pathes(values, tree, child_index, child)
            maximum = max(maximum, MaxPath.dp[child_index])
        
        MaxPath.dp[child] += maximum
        

if __name__ == '__main__':
    
    obj = MakeTree(depth=2)
    tree = obj.tree
    values = obj.values
    print(values)
    obj = MaxPath()
    obj.find_sum_pathes(values, tree, 1, 0)
    print(MaxPath.dp)
    print('Result is :', max(MaxPath.dp))
    




