import random
from typing import List


class Sorting:

    @staticmethod
    def bubbleSort(alist: List[int]) -> List[int]:
        """
        bubbleSort is basic data structure algorithm in list.
    
        Bubble sort is a sorting algorithm that compares two adjacent
        elements and swaps them until they are not in the intended order.

        Args:
            alist List[int]: [5, 8, 12, -1, 4, 3]

        Returns:
            List[int]: [-1, 3, 4, 5, 8, 12]
        """

        x = len(alist)
        for i in range(x):
            for j in range(i + 1, x):
                if alist[i] > alist[j]:
                    alist[i], alist[j] = alist[j], alist[i]

        return alist

    @staticmethod
    def quickSort(alist: List[int]) -> List[int]:
        """
        quickSort is basic data structure algorithm in list.

        Quick Sort is a sorting algorithm, which is commonly used in computer science.
        Quick Sort is a divide and conquer algorithm.

        Args:
            alist List[int]: [5, 8, 12, -1, 4, 3]

        Returns:
            List[int]: [-1, 3, 4, 5, 8, 12]
        """

        if len(alist) <= 1:
            return alist

        pivot = random.choice(alist)
        lt = [v for v in alist if v < pivot]
        eq = [v for v in alist if v == pivot]
        gt = [v for v in alist if v > pivot]

        return Sorting.quickSort(lt) + eq + Sorting.quickSort(gt)

    @staticmethod
    def selectionSort(alist: List[int]) -> List[int]:
        """

        Selection sort is a simple sorting algorithm.
        This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts,
        the sorted part at the left end and the unsorted part at the right end.
        Initially, the sorted part is empty and the unsorted part is the entire list.

        Args:
            alist List[int]: [5, 8, 12, -1, 4, 3]

        Returns:
            List[int]: [-1, 3, 4, 5, 8, 12]
        """
        for i in range(0, len(alist)):
            min_value = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[min_value]:
                    min_value = j

            alist[i], alist[min_value] = alist[min_value], alist[i]

        return alist
