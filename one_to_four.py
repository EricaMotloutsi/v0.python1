def one_to_four():
    for i in range(1,5):
        print(i)

# Write a function `one_to_four` that prints the numbers 1 through 4 (inclusive).


one_to_four()

def count_up(max):
    for i in range(1, max+1):
        print(i)

        count_up(5)
        count_up(3)

def evens(max_num):
    for num in range(2, max_num):
        if num % 2 == 0:
            print(num)


evens(11)
evens(8)

