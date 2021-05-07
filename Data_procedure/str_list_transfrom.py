#
# https://blog.csdn.net/roytao2/article/details/53433373

# tuple or list to str
k = (-70, 15, -60, 26)
b = list(map(lambda x: str(x), k))
str_b = ",".join(b)
print(b)

# str to tuple
tuple_b = tuple(str_b.split(","))
