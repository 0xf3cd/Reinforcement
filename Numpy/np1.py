import numpy as np

# numpy 的操作对象是数组（矩阵）

# 创建 a b 两个数组
a = np.array([1, 2, 3])		# 一维数组，即为 1 * 3 的矩阵
# a = np.ndarray([1, 2, 3]) 也 OK，但是不推荐使用 ndarray 来创建
# 之后都使用 array 来创建
b = np.array([[1, 2, 3], 	
			  [4, 5, 6]])	# 二维数组，即为 2 * 3 的矩阵

# 可以在创建数组的时候指定其中的数据类型
# 可选的有 int64(可以写成int) int32 float64(可以写为float) float32 
# 不指定 dtype 时，默认为 int64
c = np.array([7, 8, 9], dtype = np.float64) # 将 c 的数据类型指定为 float64

print('a:')
print(a)
print('a 的数据类型: ', end = '') 
print(a.dtype)
print()

print('b:')
print(b)
print('b 的数据类型: ', end = '')
print(b.dtype)
print()

print('c:')
print(c)
print('c 的数据类型: ', end = '') 
print(c.dtype)
print()

# 如果每一行的元素个数不一致，则会将其识别为一个一维数组，数组元素也为一个一维数组
d = np.array([[1, 2, 3],
			  [4, 5, 6],
			  [7, 8]])
print('d:')
print(d)
print('d 的数据类型: ', end = '') 
print(d.dtype)
print('d 的每一个元素都为一个一维数组(list)')
print()

# 除了 array，还可以使用 zeros ones empty 等来创建数组
# 这些方式创建出的数组的数据类型默认为 float64
allZero = np.zeros((5, 5))	# 创建一个 5 行 5 列的全零数组
allOne = np.ones((1, 2), dtype = np.int32)	# 创建一个 5 行 5 列的全一数组，指定类型为 int32
allEmpty = np.empty((3, 2))	# 创建一个 3 行 2 列的全空数组

print('allZero:')
print(allZero)
print('allZero 的默认数据类型: ', end = '') 
print(allZero.dtype)
print('它的数据类型只能保持为默认值，不能被指定')
print()

print('allOne:')
print(allOne)
print('allOne 的数据类型被显式指定为: ', end = '')
print(allOne.dtype)
print('它的数据类型可以被指定')
print()

print('allEmpty:')
print(allEmpty)
print('allEmpty 的默认数据类型: ', end = '') 
print(allEmpty.dtype)
print('全空数组的初始值都为接近于 0 的小数，它的数据类型只能保持为默认值，不能被指定')
print()

# 使用 arange linespace 创建数组，并通过 reshape 调整数组形状
arange = np.arange(10, 21, 2)	# 创建 10 - 20 间的数据，步长为 2
# 可以只给定一个参数，np.arange(x) 表示创建一个一维数组，元素为 0 1 2 ... n-1，共 n 个
linspace = np.linspace(0, 6, 10)	# 将 0 - 6 分成等间距的 10 个数据

print('arange')
print(arange)
print()

print('linspace')
print(linspace)
print()

arange2 = arange.reshape((2, 3)) # 将 arange 调整为 2 行 3 列 
print('arange2')
print(arange2)
print()

# 以上代码会出错
# arange3 = arange2.reshape((3, 1))
# 3 * 1 != 2 * 3
# 要保证 reshape 前后元素个数一致

# array 的属性
# 以 b 为例进行说明
print('b:')
print(b)
print()

print('ndim 属性表示数组（矩阵）的维度，b.ndim = ', end = '')
print(b.ndim)
print('shape 属性表示数组（矩阵）的行列值，b.shape = ', end = '')
print(b.shape)
print('size 属性表示数组（矩阵）的元素个数，b.size = ', end = '')
print(b.size)
print('dtype 属性表示数组（矩阵）的元素数据类型，b.dtype = ', end = '')
print(b.dtype)
print('itemsize 属性表示数组（矩阵）中每个元素所占字节数，b.itemsize = ', end = '')
print(b.itemsize)