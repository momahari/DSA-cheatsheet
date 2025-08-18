import sys

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        ...

    def get_level(self):
        level = 0
        node = self.parent
        while node:
            level += 1
            node = node.parent
        return level

    def print_tree(self, tree_type):
        i = 1
        if tree_type == 'designation':
            i = 0
        elif tree_type == 'name':
            i = 1
        elif tree_type == 'both':
            i = 2
        else:
            raise Exception('specify the type exactly either a designation or a name or both')
        prefix = " " * self.get_level() * 3
        prefix += "|--" if self.parent else ""
        if i < 2:
            print(prefix + f"\033[1m\033[3m{self.data[i]}\033[0m")
        else:
            print(prefix + self.data[1], f"\033[1m\033[3m({self.data[0]})\033[0m")
        if self.children:
            for child in self.children:
                child.print_tree(tree_type)

def build_tree():
    root = TreeNode('faculty')

    electrical = TreeNode('electrical')
    electrical.add_child(TreeNode('GSIT'))
    electrical.add_child(TreeNode('EI'))
    electrical.add_child(TreeNode('RE'))
    electrical.add_child(TreeNode('ME'))
    electrical.add_child(TreeNode('ER'))

    electronics = TreeNode('electronics')
    electronics.add_child(TreeNode('ES'))
    electronics.add_child(TreeNode('INST'))

    automation = TreeNode('automation')
    automation.add_child(TreeNode('robotics'))
    automation.add_child(TreeNode('API'))

    telecommunications = TreeNode('telecommunications')
    telecommunications.add_child(TreeNode('advanced telecommunications'))

    root.add_child(electrical)
    root.add_child(electronics)
    root.add_child(automation)
    root.add_child(telecommunications)

    return root

def build_management_tree():
    root = TreeNode(('CEO', 'Nilupul'))

    tech = TreeNode(('CTO', 'Chinamy'))
    subtech = TreeNode(('Infrastructure head', 'vishwa'))
    subtech.add_child(TreeNode(('Cloud manager', 'Dhaval')))
    subtech.add_child(TreeNode(('App Manager', 'Abhijit')))
    subtech2 = TreeNode(('Application head', 'Amir'))
    tech.add_child(subtech)
    tech.add_child(subtech2)

    management = TreeNode(('HR head', 'Gels'))
    management.add_child(TreeNode(('Recruitment Manager', 'Peter')))
    management.add_child(TreeNode(('Policy Manager ', 'Waqas')))

    root.add_child(tech)
    root.add_child(management)
    return root


if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree('name')
    pass
