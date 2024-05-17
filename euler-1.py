a = 0
for x in range(1, 10):
    if x%3 == 0:
        a = a + x
    elif x%5 == 0:
        a = a + x
print(a)
