import numpy as np

a = np.array([10, 20, 30 ,40])
b = np.arange(4, 0, -1)
c = np.array([[1, 2, 3, 4],
			  [5, 6, 7, 8]])
d = np.array([[8, 7, 6, 5],
			  [4, 3, 2, 1]])

print('a:')
print(a)
print('b:')
print(b)
print('c:')
print(c)
print('d:')
print(d)
print()

# 索引和分片都和 python 原生数组类似
# 索引
print('索引')
print('a[3] = ', a[3])
print('c[0][1] = ', c[0][1])
print()

# 分片
print('分片')
print('a[1: 3] = ', a[1: 3])
print()

# 遍历
print('遍历 a:')
for each in a:
	print(each)
print('遍历 c:')
for each in c:
	print(each)
print('flat遍历 c:')	# 将 c 实作一维数组进行遍历
for each in c.flat:
	print(each)
print()

# 数组可以进行加减乘除
print('加减乘除运算')
print('c + d = ', end = '')
print(c + d)
print('c - d = ', end = '')
print(c - d)
print('a * b = ', end = '')
print(a * b)	# 注意是元素相乘
print('a / b = ', end = '')
print(a / b)
print()

# 数乘操作
print('数乘运算')
print('10 * b = ', end = '')
print(10 * b)
print()

# 幂次操作
print('幂次运算')
print('a ** 2 = ', end = '')
print(a ** 2)
print()

# 三角函数
print('三角函数运算')
print('np.sin(b) = ', end = '')
print(np.sin(b))
print('np.cos(b) = ', end = '')
print(np.cos(b))
print('np.tan(b) = ', end = '')
print(np.tan(b))
print()

# 逻辑判断
print('逻辑判断')
print('c <= 4 :')
print(c <= 4)
print('a != b :')
print(a != b)
print()

# 矩阵转置
print('矩阵转置')
# 只有二维数组（或以上维度的数组）才能转置
# 一维向量需要先设定 shape 才能进行转置
# a.T 等价于 np.transpose(a)
a.shape = (1, 4)	# 执行后，a 将变成一个二维数组，但是只有 1 行
print('np.transpose(a) = ', np.transpose(a))
print('a.T = ', a.T)
print()
# b.shape = (1, 4)
print('np.transpose(b) = ', np.transpose(b))
print('b.T = ', b.T)
print()
# c 已经是多维数组，不需要再设定其 shape 属性
print('np.transpose(c) = ', np.transpose(c))
print('c.T = ', c.T)
print()

# 矩阵相乘
e = d.reshape(4, 2)
print('e:')
print(e)
print()

print('矩阵相乘（满足可乘性条件）')
print('np.dot(d, e) = ', end = '')
print(np.dot(d, e))
print('d.dot(e) = ', end = '')
print(d.dot(e))
print()

# 求和，最大值或最小值操作
print('求和，最大值或最小值操作')
print('np.sum(a) = ', np.sum(a))
print('np.max(b) = ', np.max(b))
print('对某一行或某一列求和，最大值或最小值操作')
print('np.sum(c, axis = 0) = ', np.sum(c, axis = 0))	# axis 为 0 表示对列操作
print('np.min(d, axis = 1) = ', np.min(d, axis = 1))	# axis 为 1 表示对行操作
print('求最大值或最小值的索引')
print('np.argmin(a) = ', np.argmin(a))	# a 最小值的索引
print('np.argmax(a) = ', np.argmax(a))	# a 最大值的索引
print('np.argmin(c, axis = 0) = ', np.argmin(c, axis = 0))	# a 最小值的索引
print('np.argmax(c, axis = 1) = ', np.argmax(c, axis = 1))	# a 最大值的索引

# 中位数和平均数
print('平均数')
print('np.mean(a) = a.mean() = ', np.mean(a))	# 均值
print('np.average(a) = ', np.average(a))	# 均值，a.average() 没有这种写法
print('中位数')
print('np.median(b) = ', np.median(b)) # 中位数，b.median() 没有这种写法
print()

# 还有很多不太常用的函数，需要时可以再查阅
# 用户可以自行定义函数

# 合并
print('按行合并')
print('np.vstack((a, b)) = ', np.vstack((a, b)))	# 注意需要 a b 由两层括号包裹
print()
print('按列合并')
print('np.hstack((c, d)) = ', np.hstack((c, d)))	# 注意需要 a b 由两层括号包裹
print()
print('使用 concatenate 方法合并')
# 对于一维向量 使用 concatenate 前需要先指定 shape 属性（同转置操作）
a.shape = (1, 4)
b.shape = (1, 4)
print('np.concatenate((a, b, b, a), axis = 0):')
print(np.concatenate((a, b, b, a), axis = 0))	# axis = 0 表示按行合并
print('np.concatenate((c, d, d), axis = 1):')
print(np.concatenate((c, d, d), axis = 1))	# axis = 1 表示按列合并
print()

# 分割
f = np.arange(16).reshape((4, 4))
print('f:')
print(f)
print()

print('np.split(f, 4, axis = 1):')	# 等价于 np.hsplit(A, 4)
print(np.split(f, 4, axis = 1))	# axis = 1 表示按列分割，分割成 4 等份
print('np.split(f, 2, axis = 0):')	# 等价于 np.vsplit(A, 2)
print(np.split(f, 2, axis = 0))	# axis = 0 表示按行分割，分割成 2 等份

# split 只能等分
# 如果需要不等分割，则需要使用 array_split
print('np.array_split(f, 3, axis = 1):')
print(np.array_split(f, 3, axis = 1))	# axis = 1 表示按列分割，分割成 3 份
print('np.array_split(f, 1, axis = 0):')
print(np.array_split(f, 3, axis = 0))	# axis = 0 表示按行分割，分割成 3 份
print()

# 拷贝
h = a.copy()	# 深拷贝
g = a 	# 浅拷贝
a[0][0] = 111	# 之前设定了 a.shape，a 转变了一个二维数组
print('a:')
print(a)
print('h:')
print(h)
print('g:')
print(g)
