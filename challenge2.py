import ast
import astor
from AST import AST

INPUT = "input2.py"
OUTPUT = "output2.py"


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
        try:  # Normal Function Call
            fun_name = ast.Name(id=node.func.id)
        except:  # Method Call
            return node
        new_call = ast.Call(func=ast.Name(id="wrapper"), args=[fun_name] + node.args,
                            keywords=[])
        ast.copy_location(new_call, node)
        return new_call


if __name__ == "__main__":
    tree = AST(INPUT, Transformer())
    tree.transform()
    tree.compile(OUTPUT)
