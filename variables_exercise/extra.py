num = 17

if num % 2 == 0:
    print("even")
else:
    print("odd")

num = 17

if num % 2 == 0:
    print("even")
else:
    print("odd")

password = "Code123"

if len(password) < 4:
    print("too short")
elif password.isalpha():
    print("weak")
elif password.isalnum():
    print("medium")
else:
    print("strong")

temp = 32

if temp < 0:
    print("freezing")
elif temp < 20:
    print("cold")
elif temp < 30:
    print("warm")
else:
    print("hot")

ch = "e"

if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")


ch = "e"

if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")


age = 14

if age < 13:
    print("child")
elif age < 60:
    print("adult")
elif age < 20:
    print("teen")
else:
    print("senior")


def greet():
    print("hey")
    print("programmers")

def whistle():
    print("doot")

print("first")
print("second")
greet()
print("third")
print("fourth")
whistle()

def how_many():
    return 42

print(how_many)
print(how_many())

the_answer = how_many()
print(the_answer)

def how_much():
    5   # does nothing

print(how_much())

def average(num1, num2):
    print("calculating...")
    return (num1 + num2) / 2

print(average(5, 10))
print(average(20, 26))
print(average(50, 100) + 2)

a = 21 + 3
b = 20
n = average(a, b)
print(average(n, 18))

def exclaim(s):
    capitalized = s.upper()
    return capitalized + "!!"

result = exclaim("potato")
print(result)
print(len(result))
print(result[0])
print(result[-1])






