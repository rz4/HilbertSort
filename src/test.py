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
