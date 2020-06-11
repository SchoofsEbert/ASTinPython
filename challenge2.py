import ast
import astor
from AST import AST

INPUT = "input2.py"


def print_info():
    def function_info(func):
        def argument_info(*args):
            computed = func(*args)
            string = '{}: {} -> {}'.format(func.__name__, args, computed)
            print(string)
            return computed

        return argument_info

    return function_info


class Transformer(ast.NodeTransformer):
    wrapperAST = astor.code_to_ast(print_info)

    def visit_ClassDef(self, node):
        return node  # Don't add decorators to Class methods

    def visit_Module(self, node):
        self.generic_visit(node)
        node.body.insert(0, self.wrapperAST)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        node.decorator_list.append(ast.Call(ast.Name(id="print_info"), args=[], keywords=[]))
        return node


if __name__ == "__main__":
    tree = AST(INPUT, Transformer())
    tree.transform()
    tree.execute()
