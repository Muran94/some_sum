import numpy as np

def sum_1(stop):
    """
    for文を用いて、1からstopまでの総和を求める
    """
    sum_value = 0
    for i in range(1, stop + 1):
        sum_value += i
    return sum_value

def sum_2(stop):
    """
    等差数列の和の公式を用いて、1からstopまでの総和を求める
    """
    return (stop * (stop + 1)) / 2

def sum_3(stop, start = 1):
    if stop <= start:
        return "引数の値がおかしい"

    sum_value = 0
    for i in range(start, stop + 1):
        sum_value += i

    return sum_value
