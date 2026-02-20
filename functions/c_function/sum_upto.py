#Write `sum_upto(n)`
#Return the sum of numbers from 1 → n.

print(sum_upto(5))   # 15
print(sum_upto(10))  # 55

def sum_upto(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(sum_upto(5))   # 15
print(sum_upto(10))  # 55