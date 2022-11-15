
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 5, 'six', 'seven', 'eight', 'nine', True, False, 3 + 1j, 3 - 2j}
print(f"s2 :{s2}")

print("-" * 40)
s3 = {1, 2, 3}
print(f"s3 :{s3}")

s3.add(2)
s3.add(3)
s3.add(4)
s3.add(1)
s3.add(5)
s3.add(6)
s3.add(4)
print(f"s3 :{s3}")

print("-" * 40)
s3.update([1, 2, 3])
s3.update([3, 4, 5])
s3.update([5, 6, 7])
s3.update([2, 3, 4])
s3.update([8, 9, 10])

print(f"s3 :{s3}")
print("-" * 40)
# pop, remove, discard

res = s3.pop()
print(F"res :{res}")
res = s3.pop()
print(F"res :{res}")
print(f"s3 :{s3}")

print("-" * 40)
s3.remove(5)
s3.remove(10)
print(f"s3 :{s3}")

# s3.remove(1)
print("-" * 40)
s3.discard(7)
s3.remove(4)

s3.discard(1)
print(f"s3 :{s3}")

print("-" * 40)

A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")
print("-" * 40)

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 40)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 40)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 40)
print(f"A symmetric_difference B :{A ^ B}")
print(f"B symmetric_differece A :{B.symmetric_difference(A)}")

print("-" * 40)
# frozen set = immutable
fs = frozenset({1, 2, 3, 4, 5})
print(F"fs :{fs}")
print(type(fs))

# print("-" * 40)
# print(dir(fs))

