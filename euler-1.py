a = 0
for x in range(1, 1000):
    if x%3 == 0:
        a = a + x
    elif x%5 == 0:
        a = a + x
print(a)
