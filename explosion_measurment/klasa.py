import numpy as np

class Variable:
    def __init__(self, name = [], domain = []):
        self.name = name
        self.domain = domain

class Potential:
    def __init__(self, variables = np.array([]), table = np.array([])):
        self.variables = variables
        self.table = table