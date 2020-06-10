import ast
import astor


class AST:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "r") as source:
            self.AST = ast.parse(source.read())

        self.transformer = Transformer()

    def transform(self):
        self.transformer.visit(self.AST)

    def print(self):
        print(astor.dump_tree(self.AST))

    def compile(self, filename):
        with open(filename, "w") as output:
            output.write(astor.to_source(self.AST))


class Transformer(ast.NodeTransformer):
    """VISITOR FUNCTIONS"""
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

    """HELPER FUNCTIONS"""

    def is_child_of_function_definition(self, node):
        return True


if __name__ == "__main__":
    tree = AST("input1.py")
    tree.transform()
    tree.compile("output1.py")
