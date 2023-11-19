#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def check_point_in_ring(a, b):
    distance_to_origin = math.sqrt(a**2 + b**2)

    if 0.25 < distance_to_origin <= 1:
        return True
    else:
        return False

if __name__ == "__main__":
    a = float(input("Введите координату a: "))
    b = float(input("Введите координату b: "))

    if check_point_in_ring(a, b):
        print(f"Точка A({a}, {b}) принадлежит кольцу.")
    else:
        print(f"Точка A({a}, {b}) не принадлежит кольцу.")
