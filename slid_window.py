import numpy as np

i, j = np.ogrid[:3, :4] # an 3x4 array with origin on top left
x = 10 * i + j
shape = (2, 2)  # window size
step_size = 2
v = np.lib.stride_tricks.sliding_window_view(x, shape)[:, ::step_size]
print(v)