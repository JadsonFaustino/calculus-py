import matplotlib.pyplot as plt
import numpy as np

def limit(function, *approaches: tuple, delta: float = 1e-15, side: str = 'left', precision: int = 2, inf: float = 1e8):
    side = side.lower()
    assert side in ['left', 'right']

    if (side == 'right'):
        delta = -delta

    appr = ()
    for approach in approaches:
        appr = appr + (approach - delta, ) 
    L = function(*appr)
    if L > inf:
        return 'inf'
    if L < -inf:
        return '-inf'
    return round(L, precision)

def derivate(function, *points: tuple, h: float = 1e-10):
    x_h = ()
    for point in points:
        x_h = x_h + (point + h, )
    def der(*x):
        return (function(*x_h) - function(*x)) / h
    return limit(der, *points)

def integral(function, interval: tuple or list, dx: float = 1e-5, precision: int = 2, inf: float = 1e8):
    assert len(interval) == 2
    
    sum = 0
    x = interval[0]
    while (x < interval[1]):
        sum += function(x) * dx
        x += dx
    if sum > inf:
        return 'inf'
    if sum < -inf:
        return '-inf'
    return round(sum, precision)

def plot2d_function(function, interval, n_points = 1000):
    assert len(interval) == 2

    x_axis = np.linspace(interval[0], interval[1], int(n_points))
    y_axis = []
    for x in x_axis:
        y_axis.append(function(x))
    plt.figure()
    plt.plot(x_axis, y_axis)
    plt.show()

def plot2d_derivate_function(function, interval, n_points = 1000):
    assert len(interval) == 2

    x_axis = np.linspace(interval[0], interval[1], int(n_points))
    y_axis = []
    for x in x_axis:
        y_axis.append(derivate(function, x))
    plt.figure()
    plt.plot(x_axis, y_axis)
    plt.show()
    return

def func(x):
    return x ** 3

plot2d_derivate_function(func, [-5, 5])