from expression import MathExpressionEvaluator
from derivative import DerivativeCalculator
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False


def _get_plot_range(points, padding=1.0):
    if not points:
        return (-5, 5)
    min_val = min(points)
    max_val = max(points)
    range_val = max_val - min_val
    if range_val < 1e-6:
        return (min_val - padding, max_val + padding)
    return (min_val - 0.1 * range_val, max_val + 0.1 * range_val)


def SimpleIterative(expr, start):
    i = 1
    max_iter = 1000
    x_history = [start]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.ion()
    plt.show()

    while i <= max_iter:
        result = MathExpressionEvaluator.evaluate(expr, start)
        x_history.append(result)
        
        ax.clear()
        
        x_min, x_max = _get_plot_range(x_history)
        x_plot = np.linspace(x_min, x_max, 1000)
        g_plot = [MathExpressionEvaluator.evaluate(expr, x) for x in x_plot]
        ax.plot(x_plot, g_plot, label='迭代函数 φ(x)')
        ax.plot(x_plot, x_plot, 'k--', label='y = x')
        
        for j in range(len(x_history) - 1):
            x_n = x_history[j]
            x_next = x_history[j + 1]
            ax.plot([x_n, x_n], [x_n, x_next], 'r--', alpha=0.6)
            ax.plot([x_n, x_next], [x_next, x_next], 'r--', alpha=0.6)
            ax.scatter([x_n], [x_n], color='red', zorder=5)
            ax.text(x_n, x_n, f'x{j}', fontsize=9)
        
        ax.scatter([result], [result], color='green', s=100, zorder=5, label=f'x{i}')
        ax.text(result, result, f'x{i}', fontsize=10)
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'简单迭代法 - 第{i}次迭代')
        ax.grid(alpha=0.3)
        ax.legend()
        
        plt.pause(1)
        
        if abs(result - start) < 1e-5:
            root = result
            break
        print(f"第{i}次迭代结果：{result:.6f}")
        start = result
        i += 1
    else:
        raise ValueError(f"迭代{max_iter}次未收敛，可能不收敛或初值不合适")
    
    plt.ioff()
    ax.set_title(f'简单迭代法 - 收敛完成（共{i-1}次迭代）')
    plt.show()
    print(f"方程根为{root:.5f}，迭代次数为{i - 1}")


def NewtonIterative(expr, start):
    i = 1
    max_iter = 1000
    start = float(start)
    x_history = [start]
    f_history = []
    df_history = []
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.ion()
    plt.show()

    while i <= max_iter:
        f = MathExpressionEvaluator.evaluate(expr, start)
        df = DerivativeCalculator.derivative(expr, start)
        f_history.append(f)
        df_history.append(df)
        
        if abs(df) < 1e-10:
            plt.ioff()
            raise ValueError(f"第{i}次迭代时导数为零，牛顿迭代法无法继续计算，请更换初值")
        
        result = start - f / df
        x_history.append(result)
        
        ax.clear()
        
        x_min, x_max = _get_plot_range(x_history)
        x_plot = np.linspace(x_min, x_max, 1000)
        f_plot = [MathExpressionEvaluator.evaluate(expr, x) for x in x_plot]
        ax.plot(x_plot, f_plot, label='函数 f(x)')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        
        for j in range(len(x_history) - 1):
            x_n = x_history[j]
            f_n = MathExpressionEvaluator.evaluate(expr, x_n)
            df_n = DerivativeCalculator.derivative(expr, x_n)
            
            ax.scatter([x_n], [f_n], color='red', zorder=5)
            ax.text(x_n, f_n, f'x{j}', fontsize=9)
            
            tangent_y = df_n * (x_plot - x_n) + f_n
            ax.plot(x_plot, tangent_y, 'g--', alpha=0.5, label='切线' if j == 0 else "")
        
        current_f = MathExpressionEvaluator.evaluate(expr, result)
        ax.scatter([result], [current_f], color='green', s=100, zorder=5, label=f'x{i}')
        ax.text(result, current_f, f'x{i}', fontsize=10)
        
        current_df = DerivativeCalculator.derivative(expr, result)
        current_tangent = current_df * (x_plot - result) + current_f
        ax.plot(x_plot, current_tangent, 'g--', alpha=0.8)
        
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'牛顿迭代法 - 第{i}次迭代')
        ax.grid(alpha=0.3)
        ax.legend()
        
        plt.pause(1)
        
        if abs(result - start) < 1e-5:
            root = result
            break
        print(f"第{i}次迭代结果：{result:.6f}")
        start = result
        i += 1
    else:
        plt.ioff()
        raise ValueError(f"迭代{max_iter}次未收敛，可能不收敛或初值不合适")
    
    plt.ioff()
    ax.set_title(f'牛顿迭代法 - 收敛完成（共{i-1}次迭代）')
    plt.show()
    print(f"方程根为{root:.5f}，迭代次数为{i - 1}")

def AitkenIterative(expr, x):
    i = 1
    max_iter = 1000
    x_history = [x]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.ion()
    plt.show()
    
    while i <= max_iter:
        last = x
        y = MathExpressionEvaluator.evaluate(expr, last)
        z = MathExpressionEvaluator.evaluate(expr, y)
        x = (last * z - y**2) / (last + z - 2*y)
        x_history.append(x)
        
        ax.clear()
        x_min, x_max = _get_plot_range(x_history)
        x_plot = np.linspace(x_min, x_max, 1000)
        g_plot = [MathExpressionEvaluator.evaluate(expr, x) for x in x_plot]
        ax.plot(x_plot, g_plot, label='迭代函数 φ(x)')
        ax.plot(x_plot, x_plot, 'k--', label='y = x')
        
        for j, point in enumerate(x_history):
            ax.scatter([point], [point], color='red', zorder=5)
            ax.text(point, point, f'x{j}', fontsize=9)
            if j > 0:
                ax.plot([x_history[j-1], point], [x_history[j-1], point], 'b--', alpha=0.6)
        
        ax.scatter([x], [x], color='green', s=100, zorder=5, label=f'x{i}')
        ax.set_title(f'埃特肯法 - 第{i}次迭代')
        ax.grid(alpha=0.3)
        ax.legend()
        plt.pause(1)
        
        if abs(x - last) < 1e-5:
            root = x
            break
        print(f"第{i}次迭代结果：{x:.6f}")
        i += 1
    else:
        plt.ioff()
        raise ValueError(f"迭代{max_iter}次未收敛")
    
    plt.ioff()
    ax.set_title(f'埃特肯法 - 收敛完成（共{i-1}次迭代）')
    plt.show()
    print(f"方程根为{root:.5f}，迭代次数为{i - 1}")

def SingleDotIterative(expr, x0, x1):
    i = 1
    max_iter = 1000
    xn = x1
    f0 = MathExpressionEvaluator.evaluate(expr, x0)
    x_history = [x0, xn]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.ion()
    plt.show()

    while i <= max_iter:
        fn = MathExpressionEvaluator.evaluate(expr, xn)
        if abs(fn - f0) < 1e-10:
            plt.ioff()
            raise ValueError("弦截法中两点函数值相等，无法计算")
        
        result = (x0 * fn - xn * f0) / (fn - f0)
        x_history.append(result)
        
        ax.clear()
        
        x_min, x_max = _get_plot_range(x_history)
        x_plot = np.linspace(x_min, x_max, 1000)
        f_plot = [MathExpressionEvaluator.evaluate(expr, x) for x in x_plot]
        ax.plot(x_plot, f_plot, label='函数 f(x)')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        
        ax.scatter([x0], [f0], color='blue', s=80, zorder=5, label=f'固定点 x0={x0:.4f}')
        ax.text(x0, f0, f'x0', fontsize=9)
        
        for j in range(1, len(x_history)-1):
            x_prev = x_history[j]
            f_prev = MathExpressionEvaluator.evaluate(expr, x_prev)
            ax.scatter([x_prev], [f_prev], color='red', zorder=5)
            ax.text(x_prev, f_prev, f'x{j}', fontsize=9)
        
        弦线_x = [x0, xn]
        弦线_y = [f0, fn]
        ax.plot(弦线_x, 弦线_y, 'g--', label='当前弦线')
        
        current_f = MathExpressionEvaluator.evaluate(expr, result)
        ax.scatter([result], [current_f], color='green', s=100, zorder=5, label=f'x{i}')
        ax.text(result, current_f, f'x{i}', fontsize=10)
        
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'单点弦截法 - 第{i}次迭代')
        ax.grid(alpha=0.3)
        ax.legend()
        
        plt.pause(1)
        
        if abs(result - xn) < 1e-5:
            root = result
            break
        print(f"第{i}次迭代结果：{result:.6f}")
        xn = result
        i += 1
    else:
        plt.ioff()
        raise ValueError(f"迭代{max_iter}次未收敛，可能不收敛或初值不合适")
    
    plt.ioff()
    ax.set_title(f'单点弦截法 - 收敛完成（共{i-1}次迭代）')
    plt.show()
    print(f"方程根为{root:.5f}，迭代次数为{i - 1}")

def DoubleDotIterative(expr, x0, x1):
    """双点弦截法（动态更新两个点，显示迭代过程）"""
    i = 1
    max_iter = 1000
    xn = x1
    x_prev = x0
    x_history = [x_prev, xn]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.ion()
    plt.show()

    while i <= max_iter:
        f_prev = MathExpressionEvaluator.evaluate(expr, x_prev)
        fn = MathExpressionEvaluator.evaluate(expr, xn)
        
        if abs(fn - f_prev) < 1e-10:
            plt.ioff()
            raise ValueError("弦截法中两点函数值相等，无法计算")
        
        result = (x_prev * fn - xn * f_prev) / (fn - f_prev)
        x_history.append(result)
        
        ax.clear()
        
        x_min, x_max = _get_plot_range(x_history)
        x_plot = np.linspace(x_min, x_max, 1000)
        f_plot = [MathExpressionEvaluator.evaluate(expr, x) for x in x_plot]
        ax.plot(x_plot, f_plot, label='函数 f(x)')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        
        for j in range(len(x_history)-1):
            x = x_history[j]
            f = MathExpressionEvaluator.evaluate(expr, x)
            ax.scatter([x], [f], color='red', zorder=5)
            ax.text(x, f, f'x{j}', fontsize=9)
        
        弦线_x = [x_prev, xn]
        弦线_y = [f_prev, fn]
        ax.plot(弦线_x, 弦线_y, 'g--', label='当前弦线')
        
        current_f = MathExpressionEvaluator.evaluate(expr, result)
        ax.scatter([result], [current_f], color='green', s=100, zorder=5, label=f'x{i}')
        ax.text(result, current_f, f'x{i}', fontsize=10)
        
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'双点弦截法 - 第{i}次迭代')
        ax.grid(alpha=0.3)
        ax.legend()
        
        plt.pause(1)
        
        if abs(result - xn) < 1e-5:
            root = result
            break
        print(f"第{i}次迭代结果：{result:.6f}")
        x_prev, xn = xn, result
        i += 1
    else:
        plt.ioff()
        raise ValueError(f"迭代{max_iter}次未收敛，可能不收敛或初值不合适")
    
    plt.ioff()
    ax.set_title(f'双点弦截法 - 收敛完成（共{i-1}次迭代）')
    plt.show()
    print(f"方程根为{root:.5f}，迭代次数为{i - 1}")