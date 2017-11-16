def sum_1(num):
    """
    for文を用いて、1からnumまでの総和を求める
    """
    sum_value = 0
    for i in range(1, num + 1):
        sum_value += i
    return sum_value

def sum_2(num):
    """
    公式を用いて、1からnumまでの総和を求める
    """
    return (num * (num + 1)) / 2

def sum_3(stop, start = 1):
    if stop <= start:
        return "引数の値がおかしい"

    sum_value = 0
    for i in range(start, stop + 1):
        sum_value += i

    return sum_value

def sum_4(num):
    """
    再帰関数を用いて、1からnumまでの総和を求める
    """
    return num + sum_4(num - 1) if num > 0 else 0
