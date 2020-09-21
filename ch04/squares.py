#!/usr/bin/env python3
"""
Author : ncapps
Date   : 09/20/2020
Purpose: Square generator function
"""

from typing import List, Generator


# --------------------------------------------------
def squares(args: List[int]) -> Generator:
    for num in args:
        yield num ** 2


# --------------------------------------------------
def main() -> None:
    for square in squares(range(1, 6)):
        print(square)


# --------------------------------------------------
if __name__ == '__main__':
    main()
