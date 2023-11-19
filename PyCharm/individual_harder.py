#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def frenel_integral(x, epsilon=1e-10):
    result = 0.0
    n = 0

    while True:
        term = ((-1) ** n) * (x ** (4 * n + 1)) / ((2 * n + 1) * factorial(2 * n + 1))
        result += term

        if abs(term) < epsilon:
            break

        n += 1

    result *= math.sqrt(2 / math.pi)

    return result

def main():
    x = float(input("Введите значение аргумента x: "))
    epsilon = 1e-10

    result = frenel_integral(x, epsilon)

    print(f"Значение первого интеграла Френеля при x = {x}:", result)

if __name__ == "__main__":
    main()
