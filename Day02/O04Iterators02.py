
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")

iterObj = iter(l)

while True:
    try:
        elem = next(iterObj)
        print(elem)
    except StopIteration:
        break

