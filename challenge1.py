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
    def visit_FunctionDef(self, node):
        if node.name[0] != "_":
            node.name += "_1"
        return node



if __name__ == "__main__":
    ast = AST("input1.py")
    ast.transform()
    ast.compile("output1.py")
