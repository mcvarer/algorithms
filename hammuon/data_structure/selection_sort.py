from typing import List


def selectionSort(nums: List[int]) -> List[int]:
    """

    Selection sort is a simple sorting algorithm.
    This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts,
    the sorted part at the left end and the unsorted part at the right end.
    Initially, the sorted part is empty and the unsorted part is the entire list.

    Args:
        nums List[int]: [5, 8, 12, -1, 4, 3]

    Returns:
        List[int]: [-1, 3, 4, 5, 8, 12]
    """
    for i in range(0, len(nums)):
        min_value = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_value]:
                min_value = j

        nums[i], nums[min_value] = nums[min_value], nums[i]

    return nums