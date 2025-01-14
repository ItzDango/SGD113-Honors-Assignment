class VirtualForest:
    def __init__(self):
        self.trees = 0

    def plant_tree(self):
        self.trees += 1
        print(f"A new tree has been planted! Total trees: {self.trees}")

# Simulate bug fixing
def fix_bug(forest):
    # Bug fixing logic here
    forest.plant_tree()

# Example usage
forest = VirtualForest()
fix_bug(forest)
fix_bug(forest)
