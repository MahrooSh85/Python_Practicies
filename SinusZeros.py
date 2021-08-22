# find roots of August2021_0 by generator

import numpy as np

x = np.linspace(0, 100, 1000)
y = np.sin(x)


def next_root():
    for i in range(len(x)-1):
        if y[i+1]*y[i] <= 0:    # we find where the function change the sign.
            yield x[i]


generator = next_root()
for j in generator:
    print(j)
