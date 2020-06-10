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

    def execute(self):
        exec(astor.to_source(self.AST))


"""WRAPPER FUNCTION"""


def wrapper(func, *args):
    computed = func(*args)
    string = "{}: {} -> {}".format(func.__name__, args, computed)
    print(string)
    return computed


class Transformer(ast.NodeTransformer):
    wrapperAST = astor.code_to_ast(wrapper)

    def visit_Module(self, node):
        self.generic_visit(node)
        node.body.insert(0, self.wrapperAST)

    def visit_Call(self, node):
        try:  # Normal Function
            fun_name = ast.Name(id=node.func.id)
        except:  # Method
            fun_name = ast.Name(id=node.func.value)
        new_call = ast.Call(func=ast.Name(id="wrapper"), args=[fun_name] + node.args,
                            keywords=[])
        ast.copy_location(new_call, node)
        return new_call


if __name__ == "__main__":
    tree = AST("input2.py")
    tree.transform()
    # tree.print()
    tree.compile("output2.py")
