
# * O(lim) -- O(1000)
i = 1
sum = 0
while(i < 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1
print(sum)  # 233168


# * O(log lim)


def multiple(x, lim):  # O(log n)
    sum = 0
    inc = x
    while (x < lim):
        sum += x
        x += inc
    return sum


# O(log n) + O(log n) + O(log n) = 3O(log n) = O(log n)
val = multiple(3, 1000) + multiple(5, 1000) - multiple(15, 1000)
print(val)
