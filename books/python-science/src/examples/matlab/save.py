import scipy.io
import numpy as np

data = np.random.random((2, 5))
print(data)

file_path = 'data.mat'
scipy.io.savemat(file_path, {'data': data})

