"""
Abstraction of Tensor.

This uses numpy internally and has a facade to work as a node
"""
from .Node import Node


class Tensor(Node):

    @property
    def attributes(self):
        return {"color": 'orange', 'shape': 'rect'}

    def __init__(self, value):
        self.value = value

        super().__init__([])

    def forward(self):
        return self.value

    def backward(self, respect_to_node, parent_grads=None):
        raise AssertionError("Calling backward on tensor")
