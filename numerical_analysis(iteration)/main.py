import iterative

print("=" * 60)
print("\n支持函数：exp、ln、log10、log2、sin、cos、tan、asin、acos、atan、sqrt、abs等")
print("支持常数：pi（圆周率）、e（自然常数）")
print("支持运算符：+、-、*、/、**（幂）、%（取余）、//（整除）")
print("规则：使用英文字符，2×x必须写为2*x")
print("迭代方法：\n1.简单迭代法\n2.埃特肯法\n3.牛顿迭代法\n4.单点弦截法\n5.双点弦截法\n")
print("=" * 60)

method = int(input("选择迭代方法序号："))
if method == 1 or method == 2:
    expr = input("请输入迭代公式（x_{n}用x表示即可，如 exp(x) + sin(x)）：").strip()
    start = float(input("输入迭代初值："))
    if method == 1:
        print("简单迭代法：")
        iterative.SimpleIterative(expr, start)
    else:
        print("埃特肯法：")
        iterative.AitkenIterative(expr, start)
else:
    expr = input("请输入函数f(x)（含单个变量，如 exp(x) + sin(x)）：").strip()
    if method == 3:
        start = input("输入迭代初值：")
        print("牛顿迭代法：")
        iterative.NewtonIterative(expr, start)
    else:
        a = float(input("输入迭代初值1："))
        b = float(input("输入迭代初值2："))
        if method == 4:
            print("单点弦截法：")
            iterative.SingleDotIterative(expr, a, b)
        else:
            print("双点弦截法：")
            iterative.DoubleDotIterative(expr, a, b)