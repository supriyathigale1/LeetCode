"""LeetCode practice utilities.

This module contains `rearrange_spaces` which redistributes spaces
between words as required by the problem statement.
"""
from typing import List


def rearrange_spaces(text: str) -> str:
    """Rearrange spaces so that there are equal spaces between words.

    If leftover spaces remain, place them at the end. It's guaranteed
    `text` contains at least one word.
    """
    words: List[str] = text.split()
    total_spaces = text.count(' ')
    if len(words) == 1:
        return words[0] + ' ' * total_spaces
    gaps = len(words) - 1
    space_between = total_spaces // gaps
    extra = total_spaces % gaps
    return (' ' * space_between).join(words) + ' ' * extra


if __name__ == '__main__':
    sample = "  this   is  a sentence "
    print(rearrange_spaces(sample))
