import ast
import astor

class AST:
    def __init__(self, filename, transformer):
        self.filename = filename
        with open(filename, "r") as source:
            self.AST = ast.parse(source.read())

        self.transformer = transformer

    def transform(self):
        self.transformer.visit(self.AST)

    def print(self):
        print(astor.dump_tree(self.AST))

    def compile(self, filename):
        with open(filename, "w") as output:
            output.write(astor.to_source(self.AST))

    def execute(self):
        exec(astor.to_source(self.AST), {})
