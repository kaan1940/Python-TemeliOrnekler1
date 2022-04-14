x = int(input())
if x < 1:
    y = (3 * x) - 4
elif 1 <= x <= 10:
    y = x + 2
elif x > 10:
    y = (2 * x) + 4
print(y)