import sys

lista = list(range(100))
print(sys.getsizeof(lista))

l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))