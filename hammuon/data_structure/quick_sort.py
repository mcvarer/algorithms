import random
from typing import List


def quickSort(nums: List[int]) -> List[int]:
    """
    quickSort is basic data structure algorithm in list.

    Quick Sort is a sorting algorithm, which is commonly used in computer science. 
    Quick Sort is a divide and conquer algorithm. 

    Args:
        nums List[int]: [5, 8, 12, -1, 4, 3]

    Returns:
        List[int]: [-1, 3, 4, 5, 8, 12]
    """
    
    if len(nums) <= 1:
        return nums
    
    pivot = random.choice(nums)
    lt = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    gt = [v for v in nums if v > pivot]
    
    return quickSort(lt) + eq + quickSort(gt)