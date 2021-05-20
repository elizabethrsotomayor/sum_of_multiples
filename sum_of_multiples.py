from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """Return the sum of the multiples of unique numbers up to but not including the number."""
    sum = 0

    # for num in range(limit, 0, -1):
    #     # if num % multiples[0] == 0:
    #     #     sum += num
    #     #     print(sum, num)
    #     for i in multiples:
    #         # print(num, i)
    #         if num % i == 0:
    #             sum += num



    return sum


# print(sum_of_multiples(7, [3])) # 9
# print(sum_of_multiples(4, [3, 5])) # 3
# print(sum_of_multiples(20, [7, 13, 17]))  # 51
print(sum_of_multiples(150, [5, 6, 8])) # 4419
print(sum_of_multiples(20, [3,5])) # 78
