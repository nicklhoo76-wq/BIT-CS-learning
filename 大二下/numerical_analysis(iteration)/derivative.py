from expression import MathExpressionEvaluator

class DerivativeCalculator:
    @staticmethod
    def derivative(expr, x):
        """
        用中心差分法计算函数在x处的导数
        :param expr: 函数表达式字符串
        :param x: 计算导数的点
        :return: 导数值
        """
        h=1e-5
        # 计算x+h和x-h处的函数值
        f_x_plus_h = MathExpressionEvaluator.evaluate(expr, x + h)
        f_x_minus_h = MathExpressionEvaluator.evaluate(expr, x - h)
        
        # 中心差分公式：f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
        derivative_value = (f_x_plus_h - f_x_minus_h) / (2 * h)
        return derivative_value