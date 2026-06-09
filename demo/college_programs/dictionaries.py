d = {1: "a", 2: "b", 3: "c"}
print(d)
d2 = d.copy()
print(d2)
d[4] = "d"
print(d)
d.pop(3)
print(d)
d.update({2: "x"})
print(d)
print(d.keys())
print(d.values())
print(d.get(1))
del d[4]
print(d)
d2.clear()
print(d2)
