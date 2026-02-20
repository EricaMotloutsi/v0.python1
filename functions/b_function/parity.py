# Write a function `parity` that accepts a number.
# Return the string "even" if the number is even.
# Return the string "odd" if the number is odd.

     # Write a function `parity` that accepts a number.
# Return the string "even" if the number is even.
# Return the string "odd" if the number is odd.

print(parity(5))       # "odd"
print(parity(7))       # "odd"
print(parity(13))      # "odd"
print(parity(32))      # "even"
print(parity(10))      # "even"
print(parity(602348))  # "even"

def parity(num):
    if num % 2 ==0:
        return "even"
    else:
        return "odd"
print(parity(5))

print(parity(5))       # "odd"
print(parity(7))       # "odd"
print(parity(13))      # "odd"
print(parity(32))      # "even"
print(parity(10))      # "even"
print(parity(602348))

