# Basic Data Structure Algorithms

## Installing

```bash
pip install hammuon
``` 
or 
```bash
pip install -e git+https://github.com/mcvarer/algorithms.git#egg=hammuon
```

### Usage
```python
from hammuon.data_structure.sortings import Sorting

ss = Sorting()
print(ss.quickSort([8, 12, 55, -12]))
print(ss.bubbleSort([8, 12, 55, -12]))
print(ss.selectionSort([8, 12, 55, -12]))

```

### Output
```bash
[-12, 8, 12, 55]
```