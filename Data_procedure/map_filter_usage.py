# filter: filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，
# 最后将返回 True 的元素放到新列表中。
print(list(filter(lambda x: x % 2 == 0, range(10))))

# map: map() 会根据提供的函数对指定序列做映射.
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# map(func, *iterables) --> map object
print(list(map(lambda x: 2 * x, range(10))))
