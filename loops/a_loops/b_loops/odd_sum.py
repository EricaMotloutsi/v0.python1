# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

def odd_sum(max_num):
    sum = 1
    for n in range(1, max_num+1):
          if n % 2 != 0:
                   sum = sum * n 
                   print(sum)

odd_sum(10)
odd_sum(5)

