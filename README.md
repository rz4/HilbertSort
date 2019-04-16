# HilbertSort

Author: Rafael Zamora-Resendiz

## Overview
This project contains a Python implementation of HilbertSort for sorting points in Euclidean
space using space-filling curves. Space filling curves are 1-dimensional
traversals of n-dimensional space where each point in a discrete space is visited
once. These family of curves have been heavily researched in the past for their
locality preserving properties and are especially useful for dimensionality reduction.

Here, we explore Hilbert's famous curve to impose an ordering on a set of points
in 3D space. The sorting of points along the traversal of the space filling curve allows
for efficient point cloud reduction using sequence-based averaging while still
maintaining the global structure of the cloud.

For more information about HilbertSort for point cloud reduction, please refer to
the project's Jupyter [notebook](notebooks/research.ipynb)

## Importing Algorithm

```python
# test.py
import numpy as np
from hilbertsort import HilbertSort3D

if __name__ == '__main__':

    # Parameters
    bins = 32
    radius = 50
    origin = (0,0,0)

    # Initiate Sorter
    sorter = HilbertSort3D(origin=origin, radius=radius, bins=bins)

    # Load Data
    data = np.random.uniform(-50, 50, (100,3))
    print("Unsorted Points:\n", data)

    # Perform Hilbert Sort
    sorted_data = sorter.sort(data)
    print("Sorted Points:\n", sorted_data)
```
