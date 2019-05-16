class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        return self.pre_order

    @property
    def pre_order(self):
        yield self
        if self.left:
            yield from self.left

        if self.right:
            yield from self.right
