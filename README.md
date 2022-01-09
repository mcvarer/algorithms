# Basic Data Strcutre Algorithms

## Installing

```bash
pip install hammuon
``` 
or 
```bash
pip install -e git+https://github.com/mcvarer/algorithms.git#egg=hammuon
```


## 1. Quick Sort
Quick Sort is a sorting algorithm, which is commonly used in computer science. 
Quick Sort is a divide and conquer algorithm. 

### Usage
```python
from hammuon.data_structure.quick_sort import quickSort

print(quickSort([8, 12, 55, -12]))
```

### Output
```bash
[-12, 8, 12, 55]
```

## 2. Bubble Sort
Bubble sort is a sorting algorithm that compares two adjacent
elements and swaps them until they are not in the intended order.

### Usage
```python
from hammuon.data_structure.bubble_sort import bubbleSort

print(bubbleSort([8, 12, 55, -12]))
```

### Output
```bash
[-12, 8, 12, 55]
```

## 3. Selection Sort
Selection sort is a simple sorting algorithm.

### Usage
```python
from hammuon.data_structure.selection_sort import selectionSort

print(selectionSort([8, 12, 55, -12]))
```

### Output
```bash
[-12, 8, 12, 55]
```