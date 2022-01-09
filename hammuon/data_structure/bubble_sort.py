from typing import List


def bubbleSort(nums: List[int]) -> List[int]:
    """
    bubbleSort is basic data structure algorithm in list.

    Bubble sort is a sorting algorithm that compares two adjacent 
    elements and swaps them until they are not in the intended order.

    Args:
        nums List[int]: [5, 8, 12, -1, 4, 3]

    Returns:
        List[int]: [-1, 3, 4, 5, 8, 12]
    """    
    
    x = len(nums)
    for i in range(x):
        for j in range(i+1, x):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                
    return nums