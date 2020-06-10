import ast
from AST import AST

INPUT = "input1.py"
OUTPUT = "output1.py"


class Transformer(ast.NodeTransformer):
    inside_function = False

    def visit_Constant(self, node):
        if isinstance(node.value, int) and self.inside_function:
            node.value *= -1
        return node

    def visit_FunctionDef(self, node):
        if node.name[0] != "_":
            node.name += "_1"
            self.inside_function = True
            self.generic_visit(node)
        self.inside_function = False
        return node


if __name__ == "__main__":
    tree = AST(INPUT, Transformer())
    tree.transform()
    tree.compile(OUTPUT)
