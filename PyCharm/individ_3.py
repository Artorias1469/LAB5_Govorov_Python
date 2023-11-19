#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_cells(initial_cells, time_hours):
    divisions = time_hours // 3

    final_cells = initial_cells * (2 ** divisions)

    return final_cells

if __name__ == "__main__":
    initial_cells = 1

    time_hours = 6

    result = calculate_cells(initial_cells, time_hours)

    print(f"Через {time_hours} часов будет {result} клеток.")
