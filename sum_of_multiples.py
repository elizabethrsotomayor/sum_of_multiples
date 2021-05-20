from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """Return the sum of the multiples of unique numbers up to but not including the number."""
    total = 0

    lst = []

    for num in range(limit - 1, 0, -1):
        for i in multiples:
            if i != 0:
                if num % i == 0:
                    lst.append(num)
            else:
                break

    remove_duplicates = list(dict.fromkeys(lst))

    for i in remove_duplicates:
        total += i

    return total
