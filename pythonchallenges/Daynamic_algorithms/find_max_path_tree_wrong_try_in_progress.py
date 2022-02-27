import random


class Tree():

    def __init__(self, length=5):
        self.length = length
        self.tree = self.generate_tree_sample()

    def generate_tree_sample(self):
        tree = list()
        [tree.append(random.sample(range(1, 1000), i)) for i in range(1, self.length)]
        return tree

class MaxPath(Tree):

    def find_max_path(self):
        print(self.tree)
        path_values = list()
        for row_index, row in enumerate(self.tree):
            max_row_value = max(row)

            path_values.append(self.path_value(row_index, max_row_value))

            #print(index, row)

    def path_value(self, row_index, max_row_value):
        path_sum = max_row_value
        value_index = self.tree[row_index].index(max_row_value)

        print(self.tree, max_row_value, value_index)

        for row in self.tree[row_index+1:]:
            max_value = max(row[value_index], row[value_index+1])
            print("max_value: ---> ", max_value, "path_sum: --->", path_sum, "max_between :",row[value_index], row[value_index+1])
            path_sum += max_value
            value_index = row.index(max_value)

        for row in self.tree[:row_index-1]
            pass

    def gather_up_down(self):
        for row in self.tree[row_index+1:]:
            max_value = max(row[value_index], row[value_index+1])
            print("max_value: ---> ", max_value, "path_sum: --->", path_sum, "max_between :",row[value_index], row[value_index+1])
            path_sum += max_value
            value_index = row.index(max_value)

        return path_sum

    def pather_down_up(self):
        pass










