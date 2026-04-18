import ast
import math

class MathExpressionEvaluator(ast.NodeTransformer):
    ALLOWED_FUNCTIONS = {
        "exp": "math.exp",
        "ln": "math.log",
        "log10": "math.log10",
        "log2": "math.log2",
        "sin": "math.sin",
        "cos": "math.cos",
        "tan": "math.tan",
        "asin": "math.asin",
        "acos": "math.acos",
        "atan": "math.atan",
        "sqrt": "math.sqrt",
        "abs": "abs",
        "tanh": "math.tanh",
    }
    ALLOWED_CONSTANTS = {
        "pi": "math.pi",
        "e": "math.e",
    }
    ALLOWED_BIN_OP = {ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.FloorDiv}
    ALLOWED_UNARY_OP = {ast.USub, ast.UAdd}

    def visit_Call(self, node):
        if not isinstance(node.func, ast.Name) or node.func.id not in self.ALLOWED_FUNCTIONS:
            raise ValueError(f"不允许的函数：{node.func.id}（支持：{list(self.ALLOWED_FUNCTIONS.keys())}）")
        func_path = self.ALLOWED_FUNCTIONS[node.func.id].split(".")
        new_func = ast.Attribute(
            value=ast.Name(id=func_path[0], ctx=ast.Load()),
            attr=func_path[1],
            ctx=ast.Load()
        ) if len(func_path) == 2 else ast.Name(id=func_path[0], ctx=ast.Load())
        new_args = [self.visit(arg) for arg in node.args]
        new_keywords = [self.visit(kw) for kw in node.keywords]
        return ast.Call(func=new_func, args=new_args, keywords=new_keywords)

    def visit_Name(self, node):
        if node.id in self.ALLOWED_CONSTANTS:
            const_path = self.ALLOWED_CONSTANTS[node.id].split(".")
            return ast.Attribute(
                value=ast.Name(id=const_path[0], ctx=ast.Load()),
                attr=const_path[1],
                ctx=ast.Load()
            )
        return node
    
    def visit_BinOp(self, node):
        if type(node.op) not in self.ALLOWED_BIN_OP:
            op_map = {"Add": "+", "Sub": "-", "Mult": "*", "Div": "/", "Pow": "**", "Mod": "%", "FloorDiv": "//"}
            raise ValueError(f"不允许的运算符：{type(node.op).__name__}（支持：{[op_map[op.__name__] for op in self.ALLOWED_BIN_OP]}）")
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        return node

    def visit_UnaryOp(self, node):
        if type(node.op) not in self.ALLOWED_UNARY_OP:
            raise ValueError(f"不允许的一元运算符：{type(node.op).__name__}（仅支持 +、-）")
        node.operand = self.visit(node.operand)
        return node
    
    def visit_Attribute(self, node):
        if (isinstance(node.value, ast.Name) and node.value.id == "math" 
            and node.attr in [v.split(".")[-1] for v in self.ALLOWED_FUNCTIONS.values()] + 
                            [v.split(".")[-1] for v in self.ALLOWED_CONSTANTS.values()]):
            return node
        raise ValueError(f"不允许访问属性：{node.value.id}.{node.attr}")

    @classmethod
    def evaluate(cls, expr_str, var_value):
        var_name = 'x'
        try:
            expr_str = expr_str.replace(" ", "")
            if not expr_str:
                raise ValueError("表达式不能为空！")
            
            tree = ast.parse(expr_str, mode="eval")
            transformer = cls()
            transformed_tree = transformer.visit(tree)
            ast.fix_missing_locations(transformed_tree)
            
            compiled = compile(transformed_tree, filename="<single_var_expr>", mode="eval")
            result = eval(compiled, {"math": math, "abs": abs}, {var_name: var_value})
            return result

        except SyntaxError as e:
            raise ValueError(f"语法错误！位置：第{e.lineno}行第{e.offset}列\n可能原因：括号未成对、幂运算未用**、漏写*（如2x→2*x）")
        except ZeroDivisionError:
            raise ValueError("错误：表达式中存在除以零！")
        except (ValueError, ArithmeticError) as e:
            raise ValueError(f"计算错误：{str(e)}（可能是函数超出定义域，如ln(负数)、asin(>1)）")
        except NameError as e:
            name = str(e).split("'")[1]
            raise ValueError(f"未定义的名称：{name}（可能是函数/变量名错误）")
        except TypeError as e:
            raise ValueError(f"类型错误：{str(e)}（可能是函数参数类型不正确）")
        except Exception as e:
            raise ValueError(f"计算失败：{str(e)}")