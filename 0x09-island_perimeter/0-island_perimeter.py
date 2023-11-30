#!/usr/bin/python3

"""Create a function"""


def island_perimeter(grid):
    """Function that returns the perimeter of the island"""
    perimeter = 0

    rows, cols = len(grid), len(grid[0])

    def is_water_or_outside(r, c):
        """Function to determine water position"""
        return r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if is_water_or_outside(r-1, c):
                    perimeter += 1
                if is_water_or_outside(r+1, c):
                    perimeter += 1
                if is_water_or_outside(r, c-1):
                    perimeter += 1
                if is_water_or_outside(r, c+1):
                    perimeter += 1

    return perimeter
