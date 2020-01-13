import scipy.io

file_path = 'data.mat'
mat = scipy.io.loadmat(file_path)
data = mat['data']
print(type(data))
print(data)

